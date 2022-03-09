
#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

from sqlalchemy import null


class User(object):

    def __init__(self, username):
        """
        Gets the HTML page of a given user and sets basic user values

        """

        self.username = username
        req = Request('https://www.albumoftheyear.org/user/{}'.format(username), headers={'User-Agent': 'Mozilla/6.0'})
        ugly_user_page = urlopen(req).read()
        self.user_page = BeautifulSoup(ugly_user_page, 'html.parser')

        self.set_ratings()
        self.set_reviews()
        self.set_lists()
        self.set_followers()
        self.set_about()
        self.set_rating_distribution()

    def set_ratings(self):
        ratings_section = self.user_page.find(href='/user/{}'.format(self.username)+'/ratings/')
        ratings =  ratings_section.find(class_='profileStat').getText()
        self.ratings = ratings

    def get_ratings(self):
        return self.ratings

    def get_ratings_json(self):
        ratings_JSON = {
            "ratings": self.ratings
        }
        return json.dumps(ratings_JSON)

    def set_reviews(self):
        reviews_section = self.user_page.find(href='/user/{}'.format(self.username)+'/reviews/')
        reviews =  reviews_section.find(class_='profileStat').getText()
        self.reviews = reviews

    def get_reviews(self):
        return self.reviews
    
    def get_reviews_JSON(self):
        reviews_JSON = {
            "reviews": self.reviews
        }
        return json.dumps(reviews_JSON)

    def set_lists(self):
        lists_section = self.user_page.find(href='/user/{}'.format(self.username)+'/lists/')
        lists =  lists_section.find(class_='profileStat').getText()
        self.lists = lists

    def get_lists(self):
        return self.lists

    def get_lists_JSON(self):
        lists_JSON = {
            "lists": self.lists
        }
        return json.dumps(lists_JSON)

    def set_followers(self):
        followers_section = self.user_page.find(href='/user/{}'.format(self.username)+'/followers/')
        followers =  followers_section.find(class_='profileStat').getText()
        self.followers = followers

    def get_followers(self):
        return self.followers

    def get_followers_JSON(self):
        followers_JSON = {
            "followers": self.followers
        }
        return json.dumps(followers_JSON)

    def set_about(self):
        about =  self.user_page.find(class_='aboutUser').getText()
        self.about = about

    def get_about(self):
        return self.about

    def get_about(self):
        about_JSON = {
            "about_user": self.about
        }
        return json.dumps(about_JSON)

    def get_rating_distribtion(self):
        return self.rating_distribution

    def get_rating_distribtion(self):
        user_rating_distribution = self.rating_distribution

        for i in range(10):
            if (i == 0 or i == 10) and user_rating_distribution[i][3:] == "":
                user_rating_distribution[i] += '0'
            elif user_rating_distribution[i][5:] == "":
                user_rating_distribution[i] += '0'

        user_rating_distribution_JSON = {
            "100"   : user_rating_distribution[0][3:], #[key][substring]
            "90-99" : user_rating_distribution[1][5:],
            "80-89" : user_rating_distribution[2][5:],
            "70-79" : user_rating_distribution[3][5:],
            "60-69" : user_rating_distribution[4][5:],
            "50-59" : user_rating_distribution[5][5:],
            "40-49" : user_rating_distribution[6][5:],
            "30-39" : user_rating_distribution[7][5:],
            "20-29" : user_rating_distribution[8][5:],
            "10-19" : user_rating_distribution[9][5:],
            "0-9"   : user_rating_distribution[10][3:]
        }
        return json.dumps(user_rating_distribution_JSON)

    def set_rating_distribution(self):
        user_rating_distribution_tags = self.user_page.findAll(class_='distRow')
        print(user_rating_distribution_tags[0])

        user_rating_distribution = []
        user_rating_distribution.append(user_rating_distribution_tags[0].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[1].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[2].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[3].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[4].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[5].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[6].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[7].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[8].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[9].getText().encode('ascii', 'ignore').decode())
        user_rating_distribution.append(user_rating_distribution_tags[10].getText().encode('ascii', 'ignore').decode())
        self.rating_distribution = user_rating_distribution
        print(user_rating_distribution[0])