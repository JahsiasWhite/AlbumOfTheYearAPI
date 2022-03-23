from sqlalchemy import null
import pytest
from Client.client import Client

@pytest.fixture
def artist():
    return '183-kanye-west'

@pytest.mark.first
def test_initialize():
    c = Client()
    pytest.client = c
    assert pytest.client != null

def test_get_artist_albums(artist):
    artist_ratings = pytest.client.artist_albums(artist)
    assert artist_ratings != null

def test_get_artist__albums_json(artist):
    artist_ratings_json = pytest.client.artist_albums_json(artist)
    assert artist_ratings_json != null



if __name__ == "__main__":
    
    artist = '183-kanye-west'
    AlbumWrapper = Client()

    print( AlbumWrapper.artist_albums(artist) )
    
    pytest.main