from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


class UserMethods:
    """Methods for gettting a user's profile data"""


class UserMethods:
    def __init__(self):
        self.user = ""
        self.url = ""

    def __set_user_page(self, user, url):
        self.user = user
        self.url = url
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
        ugly_user_page = urlopen(self.req).read()
        self.user_page = BeautifulSoup(ugly_user_page, "html.parser")

    def user_rating_count(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        ratings_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/ratings/"
        )
        ratings = ratings_section.find(class_="profileStat").getText()
        return ratings

    def user_rating_count_json(self, user):
        ratings_JSON = {"ratings": self.user_rating_count(user)}
        return json.dumps(ratings_JSON)

    def user_review_count(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        reviews_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/reviews/"
        )
        reviews = reviews_section.find(class_="profileStat").getText()
        return reviews

    def user_review_count_json(self, user):
        reviews_JSON = {"reviews": self.user_review_count(user)}
        return json.dumps(reviews_JSON)

    def user_list_count(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        lists_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/lists/"
        )
        lists = lists_section.find(class_="profileStat").getText()
        return lists

    def user_list_count_json(self, user):
        lists_JSON = {"lists": self.user_list_count(user)}
        return json.dumps(lists_JSON)

    def user_follower_count(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        followers_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/followers/"
        )
        followers = followers_section.find(class_="profileStat").getText()
        return followers

    def user_follower_count_json(self, user):
        followers_JSON = {"followers": self.user_follower_count(user)}
        return json.dumps(followers_JSON)

    def user_about(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        about = self.user_page.find(class_="aboutUser").getText()
        return about

    def user_about_json(self, user):
        about_JSON = {"about_user": self.user_about(user)}
        return json.dumps(about_JSON)

    def user_rating_distribution(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        user_rating_distribution_tags = self.user_page.findAll(class_="distRow")

        user_rating_distribution = []
        for i in range(11):
            rating = (
                user_rating_distribution_tags[i]
                .getText()
                .encode("ascii", "ignore")
                .decode()
            )
            if i == 0 or i == 10:
                rating = rating[3:]
                if rating == "":
                    rating = 0
                user_rating_distribution.append(rating)
            else:
                rating = rating[5:]
                if rating == "":
                    rating = 0
                user_rating_distribution.append(rating)

        return user_rating_distribution

    def user_rating_distribution_json(self, user):
        user_rating_distribution = self.user_rating_distribution(user)

        user_rating_distribution_JSON = {
            "100": user_rating_distribution[0],
            "90-99": user_rating_distribution[1],
            "80-89": user_rating_distribution[2],
            "70-79": user_rating_distribution[3],
            "60-69": user_rating_distribution[4],
            "50-59": user_rating_distribution[5],
            "40-49": user_rating_distribution[6],
            "30-39": user_rating_distribution[7],
            "20-29": user_rating_distribution[8],
            "10-19": user_rating_distribution[9],
            "0-9": user_rating_distribution[10],
        }

        return json.dumps(user_rating_distribution_JSON)

    def user_ratings(self, user):
        url = self.user_url + user
        if self.url != url:
            self.__set_user_page(user, url)

        return self.user_page.find(class_="albumBlock").getText()

    def user_ratings_json(self, user):
        ratings_JSON = {"ratings": self.user_ratings(user)}
        return json.dumps(ratings_JSON)

    def user_perfect_scores(self, user):
        """Returns a list of the users perfect scores"""

        url = self.user_url + user + "/ratings/perfect/"
        if self.url != url:
            self.__set_user_page(user, url)

        perfect_scores = self.user_page.find(class_="albumBlock")
        if perfect_scores == None:
            return ""
        return perfect_scores.getText()

    def user_perfect_scores_json(self, user):
        """Returns a list of the users perfect scores in JSON format"""

        perfect_sccores_json = {"perfect scores": self.user_perfect_scores(user)}
        return json.dumps(perfect_sccores_json)

    def user_liked_music(self, user):
        """Returns a list of the users liked music"""

        url = self.user_url + user + "/liked/albums/"
        if self.url != url:
            self.__set_user_page(user, url)

        liked_music = self.user_page.find_all(class_="albumBlock")

        result = []
        for entry in liked_music:
            artist = (
                entry.find(class_="artistTitle")
                .getText()
                .encode("ascii", "ignore")
                .decode()
            )  # Gets rid of weird characters
            album = (
                entry.find(class_="albumTitle")
                .getText()
                .encode("ascii", "ignore")
                .decode()
            )
            combined = artist + ": " + album
            result.append(combined)

        return result

    def user_liked_music_json(self, user):
        """Returns a list of the users liked music in JSON format"""

        liked_music_json = {"liked music": self.user_liked_music(user)}
        return json.dumps(liked_music_json)
