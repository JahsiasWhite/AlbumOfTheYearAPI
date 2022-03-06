
#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

from sqlalchemy import null


class User(object):

    def __init__(self, username):
        """
        Gets the HTML page of a given user

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


    def get_user_ratings(self):
        return self.user_ratings

    def set_user_ratings(self):
        ratings_section = self.user_page.find(href='/user/{}'.format(self.username)+'/ratings/')
        ratings =  ratings_section.find(class_='profileStat').getText()
        ratings_JSON = {
            "ratings": ratings
        }
        self.user_ratings = json.dumps(ratings_JSON)

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