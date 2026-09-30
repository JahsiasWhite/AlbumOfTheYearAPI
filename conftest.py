"""Shared pytest config for live albumoftheyear.org tests."""

import os
from pathlib import Path

import pytest

from albumoftheyearapi.http import CloudflareBlockedError, fetch_html


PROBE_URL = "https://www.albumoftheyear.org/"


def _load_dotenv():
    """Load workspace .env so Testing tab / pytest see AOTY_COOKIES without manual export."""
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()


def _site_is_blocked():
    try:
        fetch_html(PROBE_URL)
        return False
    except CloudflareBlockedError:
        return True
    except Exception:
        # Treat unexpected network failures like a block for live tests.
        return True


@pytest.fixture(scope="session")
def aoty_reachable():
    """True when albumoftheyear.org can be fetched without Cloudflare blocking."""
    return not _site_is_blocked()


@pytest.fixture(autouse=True)
def skip_when_cloudflare_blocks(request, aoty_reachable):
    """Skip live integration tests while Cloudflare is challenging requests."""
    if request.node.get_closest_marker("unit"):
        return
    if not aoty_reachable:
        pytest.skip(
            "albumoftheyear.org is currently behind a Cloudflare bot challenge; "
            "live tests are skipped until the site allows automated access again."
        )
