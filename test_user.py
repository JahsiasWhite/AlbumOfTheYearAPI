from sqlalchemy import null
import pytest
from albumoftheyearapi import AOTY


@pytest.fixture
def user():
    return "doublez"


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
    assert user_about != null


def test_get_about_json(user):
    user_about_json = pytest.client.user_about(user)
    assert user_about_json != null


def test_get_rating_distribution(user):
    user_rating_distribution = pytest.client.user_rating_distribution(user)
    assert user_rating_distribution != null


def test_get_rating_distribution_json(user):
    user_rating_distribution_json = pytest.client.user_rating_distribution(user)
    assert user_rating_distribution_json != null


def test_get_user_ratings(user):
    user_ratings = pytest.client.user_ratings(user)
    assert user_ratings != null


def test_get_user_ratings_json(user):
    user_ratings_json = pytest.client.user_ratings(user)
    assert user_ratings_json != null


def test_get_user_perfect_scores(user):
    perfect_scores = pytest.client.user_perfect_scores(user)
    assert perfect_scores != null


def test_get_user_perfect_scores_json(user):
    perfect_scores_json = pytest.client.user_perfect_scores(user)
    assert perfect_scores_json != null


def test_get_user_liked_music(user):
    liked_music = pytest.client.user_liked_music(user)
    assert liked_music != null


def test_get_user_liked_music_json(user):
    liked_music_json = pytest.client.user_liked_music(user)
    assert liked_music_json != null


if __name__ == "__main__":

    user = "doublez"
    AlbumWrapper = AOTY()

    print("Number of ratings\n", AlbumWrapper.user_rating_count(user), "\n")
    print("Number of reviews\n", AlbumWrapper.user_review_count(user), "\n")
    print("Number of lists\n", AlbumWrapper.user_list_count(user), "\n")
    print("Follower Count\n", AlbumWrapper.user_follower_count(user), "\n")
    print("About\n", AlbumWrapper.user_about(user), "\n")
    print("Rating distribution\n", AlbumWrapper.user_rating_distribution(user), "\n")
    print("Ratings\n", AlbumWrapper.user_ratings(user), "\n")
    print("Perfect scores\n", AlbumWrapper.user_perfect_scores(user), "\n")
    print("Liked music\n", AlbumWrapper.user_liked_music(user), "\n")

    print("JSON VERSION")
    print("Number of ratings\n", AlbumWrapper.user_rating_count_json(user), "\n")
    print("Number of reviews\n", AlbumWrapper.user_review_count_json(user), "\n")
    print("Number of lists\n", AlbumWrapper.user_list_count_json(user), "\n")
    print("Follower Count\n", AlbumWrapper.user_follower_count_json(user), "\n")
    print("About\n", AlbumWrapper.user_about_json(user), "\n")
    print(
        "Rating distribution\n", AlbumWrapper.user_rating_distribution_json(user), "\n"
    )
    print("Ratings\n", AlbumWrapper.user_ratings_json(user), "\n")
    print("Perfect scores\n", AlbumWrapper.user_perfect_scores_json(user), "\n")
    print("Liked music\n", AlbumWrapper.user_liked_music_json(user), "\n")

    pytest.main
