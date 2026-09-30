"""Shared HTTP helpers for fetching albumoftheyear.org pages."""

import os
import time
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "sec-ch-ua": '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Cloudflare often binds cf_clearance to the browser User-Agent that solved it.
_session_cookies = {}
_session_user_agent = None
_last_request_at = 0.0

# Spacing + retries keep live scrapes (and the test suite) under AOTY rate limits.
DEFAULT_MIN_REQUEST_INTERVAL = 0.75
DEFAULT_MAX_RETRIES = 5


class CloudflareBlockedError(RuntimeError):
    """Raised when albumoftheyear.org returns a Cloudflare bot challenge."""

    def __init__(self, url, detail=None):
        self.url = url
        message = (
            "albumoftheyear.org is blocking this request with a Cloudflare "
            f"challenge ({detail or 'forbidden'}). "
            "Install curl_cffi, then pass browser cookies (especially "
            "cf_clearance) via AOTY(cookies=...) or AOTY_COOKIES, using the "
            "same User-Agent as that browser. See the README. "
            f"URL: {url}"
        )
        super().__init__(message)


def normalize_cookies(cookies):
    """Accept a Cookie header string or {name: value} dict."""
    if cookies is None:
        return {}
    if isinstance(cookies, dict):
        return {str(k): str(v) for k, v in cookies.items() if v is not None}
    if isinstance(cookies, str):
        parsed = {}
        for part in cookies.split(";"):
            part = part.strip()
            if not part or "=" not in part:
                continue
            name, value = part.split("=", 1)
            parsed[name.strip()] = value.strip()
        return parsed
    raise TypeError("cookies must be a dict, Cookie header string, or None")


def set_cookies(cookies=None, user_agent=None, replace=True):
    """Store cookies (and optional User-Agent) used for subsequent fetches.

    Args:
        cookies: dict or Cookie header string (e.g. "cf_clearance=...; __cf_bm=...").
        user_agent: browser User-Agent that obtained the cookies. Cloudflare often
            rejects cf_clearance if the UA does not match.
        replace: if True, replace existing cookies; if False, merge into them.
    """
    global _session_cookies, _session_user_agent
    parsed = normalize_cookies(cookies)
    if replace or not _session_cookies:
        _session_cookies = parsed
    else:
        _session_cookies.update(parsed)
    if user_agent is not None:
        _session_user_agent = user_agent


def clear_cookies():
    """Clear session cookies and any custom User-Agent override."""
    global _session_cookies, _session_user_agent
    _session_cookies = {}
    _session_user_agent = None


def get_cookies():
    """Return a copy of the current session cookies."""
    return dict(_session_cookies)


def _cookies_from_env():
    return normalize_cookies(os.environ.get("AOTY_COOKIES"))


def _effective_cookies():
    if _session_cookies:
        return _session_cookies
    return _cookies_from_env()


def _effective_user_agent():
    if _session_user_agent:
        return _session_user_agent
    return os.environ.get("AOTY_USER_AGENT") or DEFAULT_HEADERS["User-Agent"]


def _min_request_interval():
    raw = os.environ.get("AOTY_MIN_REQUEST_INTERVAL")
    if raw is None or raw == "":
        return DEFAULT_MIN_REQUEST_INTERVAL
    return max(0.0, float(raw))


def _max_retries():
    raw = os.environ.get("AOTY_MAX_RETRIES")
    if raw is None or raw == "":
        return DEFAULT_MAX_RETRIES
    return max(0, int(raw))


def _build_headers(include_cookie_header=True):
    headers = dict(DEFAULT_HEADERS)
    headers["User-Agent"] = _effective_user_agent()
    if include_cookie_header:
        cookies = _effective_cookies()
        if cookies:
            headers["Cookie"] = "; ".join(f"{k}={v}" for k, v in cookies.items())
    return headers


def _looks_like_cloudflare(body_text, headers=None):
    headers = headers or {}
    mitigated = headers.get("Cf-Mitigated") or headers.get("cf-mitigated")
    if mitigated and "challenge" in mitigated.lower():
        return True
    lowered = body_text.lower()
    # Real AOTY pages can mention cdn-cgi assets; require challenge UI signals.
    return (
        "just a moment..." in lowered
        or "cf-browser-verification" in lowered
        or "performing security verification" in lowered
        or (
            "<title>just a moment...</title>" in lowered
            and "cdn-cgi/challenge-platform" in lowered
        )
    )


def _raise_if_cloudflare(url, body_text, headers=None, detail=None):
    if _looks_like_cloudflare(body_text, headers):
        raise CloudflareBlockedError(url, detail or "challenge page in body")


def _curl_cffi_available():
    try:
        import curl_cffi  # noqa: F401

        return True
    except ImportError:
        return False


def _throttle():
    """Space requests so a burst of scrapes is less likely to trip HTTP 429."""
    global _last_request_at
    interval = _min_request_interval()
    if interval <= 0:
        _last_request_at = time.monotonic()
        return
    now = time.monotonic()
    wait = interval - (now - _last_request_at)
    if wait > 0:
        time.sleep(wait)
    _last_request_at = time.monotonic()


def _retry_after_seconds(headers, attempt):
    """Prefer Retry-After; otherwise exponential backoff capped at 30s."""
    headers = headers or {}
    retry_after = headers.get("Retry-After") or headers.get("retry-after")
    if retry_after:
        try:
            return max(0.0, float(retry_after))
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(retry_after).timestamp()
                return max(0.0, retry_at - time.time())
            except (TypeError, ValueError, IndexError, OverflowError):
                pass
    return min(2 ** attempt, 30)


def _fetch_with_curl_cffi(url, timeout=30):
    from curl_cffi import requests as curl_requests

    headers = _build_headers(include_cookie_header=False)
    cookies = _effective_cookies()
    response = curl_requests.get(
        url,
        headers=headers,
        cookies=cookies or None,
        impersonate="chrome",
        timeout=timeout,
        allow_redirects=True,
    )
    text = response.text
    header_map = {k: v for k, v in response.headers.items()}
    if response.status_code in (403, 503) and _looks_like_cloudflare(text, header_map):
        raise CloudflareBlockedError(url, f"HTTP {response.status_code}")
    if response.status_code >= 400:
        raise HTTPError(
            url, response.status_code, response.reason, response.headers, None
        )
    _raise_if_cloudflare(url, text, header_map)
    return response.content


def _fetch_with_urllib(url, timeout=30):
    request = Request(url, headers=_build_headers())
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
            headers = response.headers
    except HTTPError as exc:
        body = exc.read() if exc.fp is not None else b""
        text = body.decode("utf-8", errors="replace")
        if exc.code in (403, 503) and _looks_like_cloudflare(text, exc.headers):
            raise CloudflareBlockedError(url, f"HTTP {exc.code}") from exc
        raise
    except URLError as exc:
        raise CloudflareBlockedError(url, str(exc.reason)) from exc

    text = body.decode("utf-8", errors="replace")
    _raise_if_cloudflare(url, text, headers)
    return body


def fetch_html(url, timeout=30):
    """Fetch a URL and return raw HTML bytes.

    Prefers curl_cffi (Chrome TLS impersonation) when installed, which is
    required for Cloudflare cookie sessions to work. Falls back to urllib.

    Uses cookies from set_cookies() or the AOTY_COOKIES environment variable.
    Spaces requests and retries HTTP 429 with backoff.

    Raises:
        CloudflareBlockedError: when Cloudflare serves a bot challenge.
        HTTPError/URLError: for other network failures.
    """
    attempts = _max_retries() + 1
    last_error = None
    for attempt in range(attempts):
        _throttle()
        try:
            if _curl_cffi_available():
                return _fetch_with_curl_cffi(url, timeout=timeout)
            return _fetch_with_urllib(url, timeout=timeout)
        except HTTPError as exc:
            last_error = exc
            if exc.code == 429 and attempt < attempts - 1:
                time.sleep(_retry_after_seconds(exc.headers, attempt))
                continue
            raise
    raise last_error
