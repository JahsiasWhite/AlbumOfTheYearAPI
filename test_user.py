from sqlalchemy import null
import pytest
from Client.client import Client

@pytest.fixture
def user():
    return 'doublez'

@pytest.mark.first
def test_initialize():
    c = Client()
    pytest.client = c
    assert pytest.client != null

def test_get_user_ratings(user):
    user_ratings = pytest.client.user_ratings(user)
    assert user_ratings != null

def test_get_user_ratings_json(user):
    user_ratings_json = pytest.client.user_ratings_json(user)
    assert user_ratings_json != null

def test_get_reviews(user):
    user_reviews = pytest.client.user_reviews(user)
    assert user_reviews != null

def test_get_reviews_json(user):
    user_reviews_json = pytest.client.user_reviews(user)
    assert user_reviews_json != null

def test_get_lists(user):
    user_lists = pytest.client.user_lists(user)
    assert user_lists != null

def test_get_lists_json(user):
    user_lists_json = pytest.client.user_lists(user)
    assert user_lists_json != null

def test_get_followers(user):
    user_followers = pytest.client.user_followers(user)
    assert user_followers != null

def test_get_followers_json(user):
    user_followers_json = pytest.client.user_followers(user)
    assert user_followers_json != null

def test_get_about(user):
    user_about = pytest.client.user_about(user)
    print(user_about)

def test_get_about_json(user):
    user_about_json = pytest.client.user_about(user)
    print(user_about_json)

def test_get_rating_distribtion(user):
    user_rating_distribution = pytest.client.user_rating_distribtion(user)
    print(user_rating_distribution)

def test_get_rating_distribtion_json(user):
    user_rating_distribution_json = pytest.client.user_rating_distribtion(user)
    print(user_rating_distribution_json)

if __name__ == "__main__":
    
    user = 'doublez'
    AlbumWrapper = Client()

    print( AlbumWrapper.user_ratings(user) )
    print( AlbumWrapper.user_reviews(user) )
    print( AlbumWrapper.user_lists(user) )
    print( AlbumWrapper.user_followers(user) )
    print( AlbumWrapper.user_about(user) )
    print( AlbumWrapper.user_rating_distribtion(user) )

    pytest.main