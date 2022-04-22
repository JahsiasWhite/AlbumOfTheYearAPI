from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


class UserMethods:
    def __init__(self):
        self.user = ""

    def __set_user_page(self, user):
        print("Making a request")
        self.user = user
        self.url = "https://www.albumoftheyear.org/user/{}".format(user)
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
        ugly_user_page = urlopen(self.req).read()
        self.user_page = BeautifulSoup(ugly_user_page, "html.parser")

    def __get_user_rating_count(self, user):
        if self.user != user:
            self.__set_user_page(user)

        ratings_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/ratings/"
        )
        ratings = ratings_section.find(class_="profileStat").getText()
        return ratings

    def user_rating_count(self, user):
        return self.__get_user_rating_count(user)

    def user_rating_count_json(self, user):
        ratings_JSON = {"ratings": self.__get_user_rating_count(user)}
        return json.dumps(ratings_JSON)

    def __get_user_review_count(self, user):
        if self.user != user:
            self.__set_user_page(user)

        reviews_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/reviews/"
        )
        reviews = reviews_section.find(class_="profileStat").getText()
        return reviews

    def user_review_count(self, user):
        return self.__get_user_review_count(user)

    def get_review_count_json(self, user):
        reviews_JSON = {"reviews": self.__get_user_review_count(user)}
        return json.dumps(reviews_JSON)

    def __get_user_list_count(self, user):
        if self.user != user:
            self.__set_user_page(user)

        lists_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/lists/"
        )
        lists = lists_section.find(class_="profileStat").getText()
        return lists

    def user_list_count(self, user):
        return self.__get_user_list_count(user)

    def user_lists_json(self, user):
        lists_JSON = {"lists": self.__get_user_list_count(user)}
        return json.dumps(lists_JSON)

    def __get_user_follower_count(self, user):
        if self.user != user:
            self.__set_user_page(user)

        followers_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/followers/"
        )
        followers = followers_section.find(class_="profileStat").getText()
        return followers

    def user_follower_count(self, user):
        return self.__get_user_follower_count(user)

    def user_follower_count_json(self, user):
        followers_JSON = {"followers": self.__get_user_follower_count(user)}
        return json.dumps(followers_JSON)

    def __get_user_about(self, user):
        if self.user != user:
            self.__set_user_page(user)

        about = self.user_page.find(class_="aboutUser").getText()
        return about

    def user_about(self, user):
        return self.__get_user_about(user)

    def user_about_json(self, user):
        about_JSON = {"about_user": self.__get_user_about(user)}
        return json.dumps(about_JSON)

    def __get_user_rating_distribution(self, user):
        if self.user != user:
            self.__set_user_page(user)

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

    def user_rating_distribtion(self, user):
        return self.__get_user_rating_distribution(user)

    def user_rating_distribtion_json(self, user):
        user_rating_distribution = self.__get_user_rating_distribution(user)

        for i in range(10):
            if (i == 0 or i == 10) and user_rating_distribution[i][3:] == "":
                user_rating_distribution[i] += "0"
            elif user_rating_distribution[i][5:] == "":
                user_rating_distribution[i] += "0"

        user_rating_distribution_JSON = {
            "100": user_rating_distribution[0][3:],  # [key][substring]
            "90-99": user_rating_distribution[1][5:],
            "80-89": user_rating_distribution[2][5:],
            "70-79": user_rating_distribution[3][5:],
            "60-69": user_rating_distribution[4][5:],
            "50-59": user_rating_distribution[5][5:],
            "40-49": user_rating_distribution[6][5:],
            "30-39": user_rating_distribution[7][5:],
            "20-29": user_rating_distribution[8][5:],
            "10-19": user_rating_distribution[9][5:],
            "0-9": user_rating_distribution[10][3:],
        }

        return json.dumps(user_rating_distribution_JSON)
