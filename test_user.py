
from sqlalchemy import null
from user import User
import pytest


@pytest.fixture
def username():
    return 'doublez'

@pytest.mark.first
def test_user_page(username):
    pytest.user = User(username)
    assert pytest.user != null

def test_get_ratings():
    user_ratings = pytest.user.get_ratings()
    assert user_ratings != null

def test_get_reviews():
    user_reviews = pytest.user.get_reviews()
    assert user_reviews == 709

def test_get_lists():
    user_lists = pytest.user.get_lists()
    assert user_lists == 7

def test_get_followers():
    user_followers = pytest.user.get_followers()
    assert user_followers != null

def test_get_about():
    user_about = pytest.user.get_about()
    print(user_about)

def test_get_rating_distribtion():
    user_rating_distribution = pytest.user.get_rating_distribtion()
    print(user_rating_distribution)

if __name__ == "__main__":
    #user = 'doublez'
    #test_instance = User()
    #soup = test_get_user_page(user)

    user = User('doublez')
    print( user.get_ratings() )
    print( user.get_reviews() )
    print( user.get_lists() )
    print( user.get_followers() )
    print( user.get_about() )
    print( user.get_rating_distribtion() )

    pytest.main