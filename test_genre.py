"""Tests for the GenreMethods class."""

import json

import pytest

from albumoftheyearapi import AOTY
from albumoftheyearapi.genre import GenreMethods, GENRE_MAP


GENRE = "7-rock"
YEAR = 2024


@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != None


# --- genre_albums ---

def test_genre_albums_returns_list():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    assert isinstance(albums, list)


def test_genre_albums_non_empty():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    assert len(albums) > 0


def test_genre_albums_have_expected_keys():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    expected_keys = {"rank", "name", "date", "score", "review_count"}
    for album in albums:
        assert expected_keys.issubset(album.keys())


def test_genre_albums_rank_is_numeric_string():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    for album in albums:
        assert album["rank"].isdigit()


def test_genre_albums_name_contains_separator():
    """Album names are formatted as 'Artist - Title'."""
    albums = pytest.client.genre_albums(GENRE, YEAR)
    for album in albums:
        assert " - " in album["name"]


def test_genre_albums_score_is_int_when_present():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    for album in albums:
        if album["score"] is not None:
            assert isinstance(album["score"], int)


def test_genre_albums_review_count_is_int_when_present():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    for album in albums:
        if album["review_count"] is not None:
            assert isinstance(album["review_count"], int)


def test_genre_albums_caches_page():
    """Calling genre_albums twice with the same args must not re-fetch."""
    pytest.client.genre_albums(GENRE, YEAR)
    cached_url = pytest.client.genre_page_url
    pytest.client.genre_albums(GENRE, YEAR)
    assert pytest.client.genre_page_url == cached_url


# --- year parameter variants ---

def test_genre_albums_default_year():
    """Omitting year should return a non-empty list for the current year."""
    albums = pytest.client.genre_albums(GENRE)
    assert isinstance(albums, list)
    assert len(albums) > 0


def test_genre_albums_all_time():
    albums = pytest.client.genre_albums(GENRE, "all")
    assert isinstance(albums, list)
    assert len(albums) > 0


def test_genre_albums_decade():
    albums = pytest.client.genre_albums(GENRE, "2010s")
    assert isinstance(albums, list)
    assert len(albums) > 0


# --- GENRE_MAP / friendly name lookup ---

def test_genre_map_friendly_name():
    """Passing a friendly name like 'rock' should resolve to the same result as the slug."""
    by_slug = pytest.client.genre_albums(GENRE, YEAR)
    by_name = pytest.client.genre_albums("rock", YEAR)
    assert len(by_slug) == len(by_name)


def test_genre_map_contains_rock():
    assert "rock" in GENRE_MAP
    assert GENRE_MAP["rock"] == GENRE


# --- genre_albums_json ---

def test_genre_albums_json_returns_string():
    result = pytest.client.genre_albums_json(GENRE, YEAR)
    assert isinstance(result, str)


def test_genre_albums_json_is_valid_json():
    result = pytest.client.genre_albums_json(GENRE, YEAR)
    parsed = json.loads(result)
    assert "albums" in parsed


def test_genre_albums_json_matches_list():
    albums = pytest.client.genre_albums(GENRE, YEAR)
    albums_json = json.loads(pytest.client.genre_albums_json(GENRE, YEAR))
    assert len(albums) == len(albums_json["albums"])


# --- standalone class (no AOTY wrapper) ---

def test_functions_without_wrapper():
    """GenreMethods works without the AOTY wrapper."""
    standalone = GenreMethods()
    albums = standalone.genre_albums(GENRE, YEAR)
    assert isinstance(albums, list)
    assert len(albums) > 0


if __name__ == "__main__":
    aoty = AOTY()

    print("Albums (2024)\n", aoty.genre_albums(GENRE, YEAR), "\n")
    print("Albums (all time)\n", aoty.genre_albums(GENRE, "all"), "\n")
    print("Albums (2010s)\n", aoty.genre_albums(GENRE, "2010s"), "\n")
    print("Albums JSON\n", aoty.genre_albums_json(GENRE, YEAR), "\n")

    pytest.main
