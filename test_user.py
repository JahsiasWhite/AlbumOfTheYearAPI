from sqlalchemy import null
import pytest
from albumoftheyearapi import AOTY

@pytest.fixture
def user():
    return 'doublez'

@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != null

def test_get_user_rating_count(user):
    user_ratings = pytest.client.user_rating_count(user)
    assert user_ratings != null

def test_get_user_rating_count_json(user):
    user_ratings_json = pytest.client.user_rating_count_json(user)
    assert user_ratings_json != null

def test_get_review_count(user):
    user_reviews = pytest.client.user_review_count(user)
    assert user_reviews != null

def test_get_review_count_json(user):
    user_reviews_json = pytest.client.user_review_count(user)
    assert user_reviews_json != null

def test_get_list_count(user):
    user_lists = pytest.client.user_list_count(user)
    assert user_lists != null

def test_get_list_count_json(user):
    user_lists_json = pytest.client.user_list_count(user)
    assert user_lists_json != null

def test_get_follower_count(user):
    user_followers = pytest.client.user_follower_count(user)
    assert user_followers != null

def test_get_follower_count_json(user):
    user_followers_json = pytest.client.user_follower_count(user)
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
    AlbumWrapper = AOTY()

    print( AlbumWrapper.user_rating_count(user) )
    print( AlbumWrapper.user_review_count(user) )
    print( AlbumWrapper.user_list_count(user) )
    print( AlbumWrapper.user_follower_count(user) )
    print( AlbumWrapper.user_about(user) )
    print( AlbumWrapper.user_rating_distribtion(user) )

    pytest.main