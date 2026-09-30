# AlbumOfTheYearWrapper

A light weight python library that acts as an API for https://www.albumoftheyear.org/
<br>
![Tests](https://github.com/JahsiasWhite/AlbumOfTheYearAPI/workflows/Tests/badge.svg)
<img alt="PyPI" src="https://img.shields.io/pypi/v/album-of-the-year-api">

## Description

Gets data from https://www.albumoftheyear.org/. The website doesn't currently provide API support so web parsing is required to obtain data. Because of this,
and according to https://www.albumoftheyear.org/robots.txt, searching and POST requests are not allowed.

## Cloudflare / browser cookies

albumoftheyear.org sits behind Cloudflare bot protection. Automated requests often
receive a `403` "Just a moment..." challenge. When that happens, this library raises
`CloudflareBlockedError`.

To get through with a browser session you need:

1. **`curl_cffi`** (pulled in via `requirements.txt`) — Cloudflare checks TLS fingerprint;
   plain `urllib`/`requests` will still fail even with valid cookies.
2. Browser **cookies** (especially `cf_clearance`) from a session that already passed the check.
3. The **same User-Agent** as that browser.

```python
from albumoftheyearapi import AOTY

client = AOTY(
    cookies="cf_clearance=...; PHPSESSID=...",  # full Cookie header from DevTools Network
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
               "(KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36",
)
print(client.artist_name("183-kanye-west"))
```

Or set env vars:

```
AOTY_COOKIES=cf_clearance=...; PHPSESSID=...
AOTY_USER_AGENT=Mozilla/5.0 ...
```

Copy the Cookie header from DevTools → Network → the document request (not the
challenge POST). Cookies expire; refresh them when requests fail again.

The client also spaces requests (`AOTY_MIN_REQUEST_INTERVAL`, default 0.75s) and
retries HTTP 429 with backoff (`AOTY_MAX_RETRIES`, default 5). Live pytest
integration tests skip automatically when Cloudflare is blocking.

## Installation

```
pip install album-of-the-year-api
```

or upgrade

```
pip install album-of-the-year-api --upgrade
```

## Usage

**Examples**

Here's a quick example of getting a specific users follower count

```
from albumoftheyearapi import AOTY

client = AOTY()
print(client.user_follower_count('jahsias'))

>> 0
```

If you don't need the full functionality, you can also import only the neccesary files

```
from albumoftheyearapi.artist import ArtistMethods

client = ArtistMethods()
print(client.artist_albums('183-kanye-west'))

>> ['Donda 2', 'Donda', 'JESUS IS KING', 'ye', 'The Life of Pablo', 'Yeezus', 'Watch the Throne', 'My Beautiful Dark Twisted Fantasy', '808s & Heartbreak', 'Graduation', 'Late Registration', 'The College Dropout']
```

Notice artists also need their unique id along with their name

Each function also is able to return the data in JSON format

```
from albumoftheyearapi import AOTY

client = AOTY()
print(client.artist_critic_score_json('183-kanye-west'))

>> {"critic_score": "73"}
```

For detailed information, refer to the [Full API Documentation](docs/api_reference.md).
