"""Tests for the RatingsMethods class."""

import json

import pytest

from albumoftheyearapi import AOTY
from albumoftheyearapi.ratings import RatingsMethods


YEAR = 2024


@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != None


# --- top_albums_by_year ---

def test_top_albums_by_year_returns_list():
    albums = pytest.client.top_albums_by_year(YEAR)
    assert isinstance(albums, list)


def test_top_albums_by_year_non_empty():
    albums = pytest.client.top_albums_by_year(YEAR)
    assert len(albums) > 0


def test_top_albums_by_year_have_expected_keys():
    albums = pytest.client.top_albums_by_year(YEAR)
    expected_keys = {"rank", "name", "date", "score", "review_count"}
    for album in albums:
        assert expected_keys.issubset(album.keys())


def test_top_albums_by_year_rank_is_numeric_string():
    albums = pytest.client.top_albums_by_year(YEAR)
    for album in albums:
        assert album["rank"].isdigit()


def test_top_albums_by_year_name_contains_separator():
    """Album names are formatted as 'Artist - Title'."""
    albums = pytest.client.top_albums_by_year(YEAR)
    for album in albums:
        assert " - " in album["name"]


def test_top_albums_by_year_score_is_int_when_present():
    albums = pytest.client.top_albums_by_year(YEAR)
    for album in albums:
        if album["score"] is not None:
            assert isinstance(album["score"], int)


def test_top_albums_by_year_review_count_is_int_when_present():
    albums = pytest.client.top_albums_by_year(YEAR)
    for album in albums:
        if album["review_count"] is not None:
            assert isinstance(album["review_count"], int)


def test_top_albums_by_year_caches_page():
    """Calling top_albums_by_year twice with the same args must not re-fetch."""
    pytest.client.top_albums_by_year(YEAR)
    cached_url = pytest.client._ratings_page_url
    pytest.client.top_albums_by_year(YEAR)
    assert pytest.client._ratings_page_url == cached_url


# --- year parameter variants ---

def test_top_albums_by_year_default_year():
    """Omitting year should return a non-empty list for the current year."""
    albums = pytest.client.top_albums_by_year()
    assert isinstance(albums, list)
    assert len(albums) > 0


def test_top_albums_by_year_all_time():
    albums = pytest.client.top_albums_by_year("all")
    assert isinstance(albums, list)
    assert len(albums) > 0


def test_top_albums_by_year_decade():
    albums = pytest.client.top_albums_by_year("2010s")
    assert isinstance(albums, list)
    assert len(albums) > 0


# --- top_albums_by_year_json ---

def test_top_albums_by_year_json_returns_string():
    result = pytest.client.top_albums_by_year_json(YEAR)
    assert isinstance(result, str)


def test_top_albums_by_year_json_is_valid_json():
    result = pytest.client.top_albums_by_year_json(YEAR)
    parsed = json.loads(result)
    assert "albums" in parsed


def test_top_albums_by_year_json_matches_list():
    albums = pytest.client.top_albums_by_year(YEAR)
    albums_json = json.loads(pytest.client.top_albums_by_year_json(YEAR))
    assert len(albums) == len(albums_json["albums"])


# --- standalone class (no AOTY wrapper) ---

def test_functions_without_wrapper():
    """RatingsMethods works without the AOTY wrapper."""
    standalone = RatingsMethods()
    albums = standalone.top_albums_by_year(YEAR)
    assert isinstance(albums, list)
    assert len(albums) > 0


if __name__ == "__main__":
    aoty = AOTY()

    print("Top Albums (2024)\n", aoty.top_albums_by_year(YEAR), "\n")
    print("Top Albums (all time)\n", aoty.top_albums_by_year("all"), "\n")
    print("Top Albums (2010s)\n", aoty.top_albums_by_year("2010s"), "\n")
    print("Top Albums JSON\n", aoty.top_albums_by_year_json(YEAR), "\n")

    pytest.main
