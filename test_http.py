"""Unit tests for HTTP helpers (no live network required)."""

from io import BytesIO
from urllib.error import HTTPError

import pytest

from albumoftheyearapi.http import (
    CloudflareBlockedError,
    _build_headers,
    _looks_like_cloudflare,
    clear_cookies,
    fetch_html,
    get_cookies,
    normalize_cookies,
    set_cookies,
)


pytestmark = pytest.mark.unit


@pytest.fixture(autouse=True)
def _reset_cookie_session(monkeypatch):
    clear_cookies()
    # Keep unit tests on the urllib path so they stay offline/deterministic.
    monkeypatch.setattr("albumoftheyearapi.http._curl_cffi_available", lambda: False)
    yield
    clear_cookies()


def test_detects_challenge_title():
    assert _looks_like_cloudflare("<title>Just a moment...</title>")


def test_detects_cf_mitigated_header():
    assert _looks_like_cloudflare("ok", {"Cf-Mitigated": "challenge"})


def test_ignores_normal_html():
    assert not _looks_like_cloudflare("<html><title>Kanye West</title></html>")


def test_normalize_cookies_from_string():
    assert normalize_cookies("cf_clearance=abc; __cf_bm=xyz") == {
        "cf_clearance": "abc",
        "__cf_bm": "xyz",
    }


def test_normalize_cookies_from_dict():
    assert normalize_cookies({"cf_clearance": "abc"}) == {"cf_clearance": "abc"}


def test_set_cookies_adds_cookie_and_user_agent_headers():
    set_cookies(
        cookies={"cf_clearance": "test-clearance"},
        user_agent="TestAgent/1.0",
    )
    headers = _build_headers()
    assert headers["Cookie"] == "cf_clearance=test-clearance"
    assert headers["User-Agent"] == "TestAgent/1.0"
    assert get_cookies()["cf_clearance"] == "test-clearance"


def test_fetch_html_sends_cookie_header(monkeypatch):
    set_cookies(cookies="cf_clearance=from-browser")
    captured = {}

    class FakeResponse:
        headers = {}

        def read(self):
            return b"<html><title>Kanye West</title></html>"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    def fake_urlopen(request, timeout=30):
        captured["cookie"] = request.get_header("Cookie")
        return FakeResponse()

    monkeypatch.setattr("albumoftheyearapi.http.urlopen", fake_urlopen)
    body = fetch_html("https://www.albumoftheyear.org/artist/183-kanye-west/")
    assert b"Kanye West" in body
    assert captured["cookie"] == "cf_clearance=from-browser"


def test_fetch_html_raises_cloudflare_on_403(monkeypatch):
    challenge = b"<html><title>Just a moment...</title></html>"

    def fake_urlopen(request, timeout=30):
        raise HTTPError(
            request.full_url,
            403,
            "Forbidden",
            {"Cf-Mitigated": "challenge", "Server": "cloudflare"},
            BytesIO(challenge),
        )

    monkeypatch.setattr("albumoftheyearapi.http.urlopen", fake_urlopen)

    with pytest.raises(CloudflareBlockedError) as exc_info:
        fetch_html("https://www.albumoftheyear.org/artist/183-kanye-west/")

    assert "Cloudflare" in str(exc_info.value)
    assert "AOTY_COOKIES" in str(exc_info.value)


def test_fetch_html_retries_on_429(monkeypatch):
    monkeypatch.setenv("AOTY_MIN_REQUEST_INTERVAL", "0")
    monkeypatch.setenv("AOTY_MAX_RETRIES", "3")
    sleeps = []
    calls = {"n": 0}

    class FakeResponse:
        headers = {}

        def read(self):
            return b"<html><title>Kanye West</title></html>"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    def fake_urlopen(request, timeout=30):
        calls["n"] += 1
        if calls["n"] < 3:
            raise HTTPError(
                request.full_url,
                429,
                "Too Many Requests",
                {"Retry-After": "0"},
                BytesIO(b"slow down"),
            )
        return FakeResponse()

    monkeypatch.setattr("albumoftheyearapi.http.urlopen", fake_urlopen)
    monkeypatch.setattr(
        "albumoftheyearapi.http.time.sleep", lambda seconds: sleeps.append(seconds)
    )

    body = fetch_html("https://www.albumoftheyear.org/artist/183-kanye-west/")
    assert b"Kanye West" in body
    assert calls["n"] == 3
    assert sleeps  # waited between throttled/retried attempts
