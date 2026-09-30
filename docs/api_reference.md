# API Documentation

## Table of Contents

- [Client / Cloudflare](#client--cloudflare)
- [Artist Methods](#artist-methods)
- [Album Methods](#album-methods)
- [User Methods](#user-methods)
- [Genre Methods](#genre-methods)
- [Ratings Methods](#ratings-methods)

## Client / Cloudflare

`AOTY(cookies=None, user_agent=None)`
<br>Main client. Optional browser session values are needed when albumoftheyear.org
serves a Cloudflare challenge.
<br>Parameters:

- cookies - Cookie header string or `{name: value}` dict (include `cf_clearance`)
- user_agent - must match the browser that obtained those cookies

`AOTY.set_cookies(cookies=None, user_agent=None, replace=True)`
<br>Update cookies / User-Agent after construction.

`AOTY.clear_cookies()`
<br>Clear session cookies for this process.

`CloudflareBlockedError`
<br>Raised when a fetch hits a Cloudflare bot challenge. Also available from
`albumoftheyearapi`.

Environment variables (optional alternative to constructor args):

- `AOTY_COOKIES`
- `AOTY_USER_AGENT`
- `AOTY_MIN_REQUEST_INTERVAL` (default `0.75`)
- `AOTY_MAX_RETRIES` (default `5`)

Requires `curl_cffi` at runtime so TLS fingerprinting matches a real browser.

## Artist Methods

An artist id is a unique number followed by the artist's display name.<br>
EX: 589-the-strokes

`artist_albums(artist)`
<br>Returns a list of all albums by an artist
<br> Parameters:

- artist - artist id

`artist_mixtapes(artist)`
<br>Returns a list of all mixtapes by an artist
<br>Parameters:

- artist - artist id

`artist_eps(artist)`
<br>Returns a list of all eps by an artist
<br>Parameters:

- artist - artist id

`artist_singles(artist)`
<br>Returns a list of all singles by an artist
<br>Parameters:

- artist - artist id

`artist_name(artist)`
<br>Returns the name of the artist
<br>Parameters:

- artist - artist id

`artist_critic_score(artist)`
<br>Returns the critic score of the artist
<br>Parameters:

- artist - artist id

`artist_user_score(artist)`
<br>Returns the user score of the artist
<br>Parameters:

- artist - artist id

`artist_total_score(artist)`
<br>Returns the average of the critic and users score of the artist
<br>Parameters:

- artist - artist id

`artist_follower_count(artist)`
<br>Returns the follower count of the artist
<br>Parameters:

- artist - artist id

`artist_details(artist)`
<br>Returns the detials of the artist
<br>Parameters:

- artist - artist id

`artist_top_songs(artist)`
<br>Returns a list of the top songs of the artist
<br>Parameters:

- artist - artist id

`artist_live_albums(artist, as_json=False)`
<br>Returns a list of all live albums by an artist
<br>Parameters:

- artist - artist id
- as_json (bool, optional): If True, returns the result as a JSON string. Defaults to False.

`artist_compilations(artist, as_json=False)`
<br>Returns a list of all compilations by an artist
<br>Parameters:

- artist - artist id
- as_json (bool, optional): If True, returns the result as a JSON string. Defaults to False.

`artist_appears_on(artist, as_json=False)`
<br>Returns a list of albums the artist appears on
<br>Parameters:

- artist - artist id
- as_json (bool, optional): If True, returns the result as a JSON string. Defaults to False.

`similar_artists(artist)`
<br>Returns a list of similar artists to the given artist
<br>Parameters:

- artist - artist id

## Album Methods

`upcoming_releases_by_limit(total)`
<br>Returns a list of size total comtaining upcoming album releases
<br>Parameters:

- total - integer

`upcoming_releases_by_page(page_number)`
<br>Returns a list of upcoming album releases on the given page idx
<br>Parameters:

- page_number - integer

`upcoming_releases_by_date(month, day)`
<br>Returns a list of upcoming album releases on the given date
<br>Parameters:

- month - integer
- day - integer

## User Methods

`user_rating_count(user)`
<br>Returns the number of ratings by a user
<br>Parameters:

- user - username

`user_review_count(user)`
<br>Returns the number of reviews by a user
<br>Parameters:

- user - username

`user_list_count(user)`
<br>Returns the number of lists by a user
<br>Parameters:

- user - username

`user_follower_count(user)`
<br>Returns the number of followers a user has
<br>Parameters:

- user - username

`user_about(user)`
<br>Returns the about page of a user
<br>Parameters:

- user - username

`user_rating_distribution(user)`
<br>Returns a list of a users rating distribution
<br>Parameters:

- user - username

`user_ratings(user, page=1)`
<br>Returns a list of the user's ratings from a single ratings page.
<br>Parameters:

- user (str): The username to fetch ratings for.
- page (int, optional): Which ratings page to fetch. Defaults to 1.

`user_ratings_all(user, max_pages=None)`
<br>Returns a list of all the user's ratings across all pages.
<br>Parameters:

- user (str): The username to fetch ratings for.
- max_pages (int, optional): Maximum number of pages to fetch. If None, fetches until no more ratings exist.
  Useful for limiting requests on users with very large rating histories.

`user_perfect_scores(user)`
<br>Returns a list of the users perfect scores
<br>Parameters:

- user - username

`user_liked_music(user)`
<br>Returns a list of the users liked music
<br>Parameters:

- user - username

`user_reviews(user, page=1, as_json=False)`
<br>Returns a list of the user's reviews from a single reviews page. Each entry contains the artist, album, rating, and review text (may be truncated for long reviews).
<br>Parameters:

- user (str): The username to fetch reviews for.
- page (int, optional): Which reviews page to fetch. Defaults to 1.
- as_json (bool, optional): If True, returns the result as a JSON string. Defaults to False.

## Genre Methods

A genre can be passed as a friendly name (e.g. `"rock"`) or as a raw slug from the URL (e.g. `"7-rock"`).
Friendly names are resolved via `GENRE_MAP`, which can be imported directly if needed:

```python
from albumoftheyearapi.genre import GENRE_MAP
```

The `year` parameter accepts a 4-digit year (`2026`), a decade (`"2020s"`), `"all"` for all-time rankings, or `None` to default to the current calendar year.

`genre_albums(genre, year=None)`
<br>Returns a ranked list of albums for the given genre and time period.
<br>Each album in the list is a dict with the following keys:

- `rank` (str) — chart position, e.g. `"1"`
- `rank` (str) — chart position, e.g. `"1"`
- `name` (str) — album title as shown on the site
- `date` (str) — release date, e.g. `"February 6, 2026"`
- `score` (int or None) — critic score, e.g. `91`
- `review_count` (int or None) — number of reviews, e.g. `34`

Parameters:

- genre (str): Friendly name (e.g. `"rock"`) or raw URL slug (e.g. `"7-rock"`). See shorthands below.
- year (str or int, optional): Year, decade, `"all"`, or `None` for the current year.

`genre_albums_json(genre, year=None)`
<br>Returns the same data as `genre_albums` serialised as a JSON string, under the key `"albums"`.
<br>Parameters:

- genre (str): Friendly name (e.g. `"rock"`) or raw URL slug (e.g. `"7-rock"`). See shorthands below.
- year (str or int, optional): Year, decade, `"all"`, or `None` for the current year.

## Ratings Methods

`top_albums_by_year(year=None)`
<br>Returns the highest critic-rated albums for a given year, decade, or all time.
<br>Each album in the list is a dict with the following keys:

- `rank` (str) — chart position, e.g. `"1"`
- `name` (str) — `"Artist - Album"` as shown on the site
- `date` (str) — release date, e.g. `"February 13, 2026"`
- `score` (int or None) — critic score, e.g. `87`
- `review_count` (int or None) — number of critic reviews, e.g. `11`

Parameters:

- year (int or str, optional): A 4-digit year (e.g. `2026`), a decade (e.g. `"2020s"`), `"all"` for all-time rankings, or `None` to use the current calendar year.

`top_albums_by_year_json(year=None)`
<br>Returns the same data as `top_albums_by_year` serialised as a JSON string, under the key `"albums"`.
<br>Parameters:

- year (int or str, optional): Same as `top_albums_by_year`.

---

### Genre Map

| Friendly name  | URL slug         |
| -------------- | ---------------- |
| `"indie rock"` | `"1-indie-rock"` |
| `"electronic"` | `"6-electronic"` |
| `"rock"`       | `"7-rock"`       |
| `"pop"`        | `"15-pop"`       |
| `"metal"`      | `"40-metal"`     |
