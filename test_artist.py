from sqlalchemy import null
import pytest
from albumoftheyearapi import AOTY


@pytest.fixture
def artist():
    return '183-kanye-west'

@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != null

def test_get_artist_albums(artist):
    artist_albums = pytest.client.artist_albums(artist)
    assert artist_albums != null

def test_get_artist__albums_json(artist):
    artist_albums_json = pytest.client.artist_albums_json(artist)
    assert artist_albums_json != null

def test_get_artist_mixtapes(artist):
    artist_mixtapes = pytest.client.artist_mixtapes(artist)
    assert artist_mixtapes != null

def test_get_artist__mixtapes_json(artist):
    artist_mixtapes_json = pytest.client.artist_mixtapes_json(artist)
    assert artist_mixtapes_json != null

def test_get_artist_eps(artist):
    artist_eps = pytest.client.artist_eps(artist)
    assert artist_eps != null

def test_get_artist__eps_json(artist):
    artist_eps_json = pytest.client.artist_eps_json(artist)
    assert artist_eps_json != null

if __name__ == "__main__":
    
    artist = '183-kanye-west'
    AlbumWrapper = AOTY()

    print( AlbumWrapper.artist_albums(artist) )
    print( AlbumWrapper.artist_mixtapes(artist) )
    print( AlbumWrapper.artist_eps(artist) )

    pytest.main