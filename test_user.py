
from sqlalchemy import null
from User import User
import pytest


@pytest.fixture
def username():
    return 'doublez'

@pytest.mark.first
def test_user_page(username):
    pytest.user = User(username)
    assert pytest.user != null

def test_get_user_ratings():
    user_ratings = pytest.user.get_user_ratings()
    assert user_ratings != null

def test_get_user_reviews():
    user_reviews = pytest.user.get_user_reviews()
    assert user_reviews == '{"reviews": "709"}'

def test_get_user_lists():
    user_lists = pytest.user.get_user_lists()
    assert user_lists == '{"lists": "7"}'

def test_get_user_followers():
    user_followers = pytest.user.get_user_followers()
    assert user_followers != null

def test_get_user_about():
    user_about = pytest.user.get_user_about()
    print(user_about)

def test_get_user_rating_distribution():
    user_rating_distribution = pytest.user.get_user_rating_distribution()
    print(user_rating_distribution)

if __name__ == "__main__":
    #user = 'doublez'
    #test_instance = User()
    #soup = test_get_user_page(user)

    user = User('doublez')
    print( user.get_user_ratings() )
    print( user.get_user_reviews() )
    print( user.get_user_lists() )
    print( user.get_user_followers() )
    print( user.get_user_about() )
    print( user.get_user_rating_distribution() )

    pytest.main