
from wrapper import User

def test_info():
    """Tests an API call to get a users info"""

    response = test_instance.info()
    #assert response['user'] == 'Kanye', "The ID should be in the response"

def test_getUserPage(user):
    response = test_instance.getUserPage(user)
    return response

def test_getUserRatings():
    response = test_instance.getUserRatings(user, soup)
    print(response)

def test_getUserReviews():
    response = test_instance.getUserReviews(user, soup)
    print(response)

def test_getUserLists():
    response = test_instance.getUserLists(user, soup)
    print(response)

def test_getUserFollowers():
    response = test_instance.getUserFollowers(user, soup)
    print(response)

def test_getUserAbout():
    response = test_instance.getUserAbout(user, soup)
    print(response)

if __name__ == "__main__":
    user = 'doublez'
    test_instance = User()
    soup = test_getUserPage(user)

    test_getUserRatings()
    test_getUserReviews()
    test_getUserLists()
    test_getUserFollowers()
    test_getUserAbout()