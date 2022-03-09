
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

        self.set_user_ratings()
        self.set_user_reviews()
        self.set_user_lists()
        self.set_user_followers()
        self.set_user_about()
        self.set_user_rating_distribution()

    def get_user_ratings(self):
        return self.user_ratings

    def get_user_ratings_json(self):
        ratings_JSON = {
            "ratings": self.ratings
        }
        return json.dumps(ratings_JSON)

    def set_user_ratings(self):
        ratings_section = self.user_page.find(href='/user/{}'.format(self.username)+'/ratings/')
        ratings =  ratings_section.find(class_='profileStat').getText()
        self.user_ratings = ratings

    def get_user_reviews(self):
        return self.user_reviews
    
    def set_user_reviews(self):
        reviews_section = self.user_page.find(href='/user/{}'.format(self.username)+'/reviews/')
        reviews =  reviews_section.find(class_='profileStat').getText()
        reviews_JSON = {
            "reviews": reviews
        }
        self.user_reviews = json.dumps(reviews_JSON)

    def get_user_lists(self):
        return self.user_lists

    def set_user_lists(self):
        lists_section = self.user_page.find(href='/user/{}'.format(self.username)+'/lists/')
        lists =  lists_section.find(class_='profileStat').getText()
        lists_JSON = {
            "lists": lists
        }
        self.user_lists = json.dumps(lists_JSON)

    def get_user_followers(self):
        return self.user_followers

    def set_user_followers(self):
        followers_section = self.user_page.find(href='/user/{}'.format(self.username)+'/followers/')
        followers =  followers_section.find(class_='profileStat').getText()
        followers_JSON = {
            "followers": followers
        }
        self.user_followers = json.dumps(followers_JSON)

    def get_user_about(self):
        return self.user_about

    def set_user_about(self):
        about_user =  self.user_page.find(class_='aboutUser').getText()
        about_user_JSON = {
            "about_user": about_user
        }
        self.user_about = json.dumps(about_user_JSON)

    def get_user_rating_distribution(self):
        return self.user_rating_distribution

    def set_user_rating_distribution(self):
        user_rating_distribution = self.user_page.findAll(class_='distRow')
        print(user_rating_distribution[0])

        rating_100 = user_rating_distribution[0].getText().encode('ascii', 'ignore')
        rating_90_through_99 = user_rating_distribution[1].getText().encode('ascii', 'ignore')
        rating_80_through_89 = user_rating_distribution[2].getText().encode('ascii', 'ignore')
        rating_70_through_79 = user_rating_distribution[3].getText().encode('ascii', 'ignore')
        rating_60_through_69 = user_rating_distribution[4].getText().encode('ascii', 'ignore')
        rating_50_through_59 = user_rating_distribution[5].getText().encode('ascii', 'ignore')
        rating_40_through_49 = user_rating_distribution[6].getText().encode('ascii', 'ignore')
        rating_30_through_39 = user_rating_distribution[7].getText().encode('ascii', 'ignore')
        rating_20_through_29 = user_rating_distribution[8].getText().encode('ascii', 'ignore')
        rating_10_through_19 = user_rating_distribution[9].getText().encode('ascii', 'ignore')
        rating_0_through_9 = user_rating_distribution[10].getText().encode('ascii', 'ignore')
        user_rating_distribution_JSON = {
            "100"   : rating_100.decode(),
            "90-99" : rating_90_through_99.decode(),
            "80-89" : rating_80_through_89.decode(),
            "70-79" : rating_70_through_79.decode(),
            "60-69" : rating_60_through_69.decode(),
            "50-59" : rating_50_through_59.decode(),
            "40-49" : rating_40_through_49.decode(),
            "30-39" : rating_30_through_39.decode(),
            "20-29" : rating_20_through_29.decode(),
            "10-19" : rating_10_through_19.decode(),
            "0-9"   : rating_0_through_9.decode()
        }
        self.user_rating_distribution = json.dumps(user_rating_distribution_JSON)