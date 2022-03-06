
#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

from sqlalchemy import null


class User(object):

    def __init__(self, username):
        """
        Gets the HTML of a given users page

        @user : username

        """

        self.username = username
        req = Request('https://www.albumoftheyear.org/user/{}'.format(username), headers={'User-Agent': 'Mozilla/6.0'})
        ugly_user_page = urlopen(req).read()
        self.user_page = BeautifulSoup(ugly_user_page, 'html.parser')

    def get_user_ratings(self):
        ratings_section = self.user_page.find(href='/user/{}'.format(self.username)+'/ratings/')
        ratings =  ratings_section.find(class_='profileStat').getText()
        ratings_JSON = {
            "ratings" : ratings
        }
        return json.dumps(ratings_JSON)
    
    def get_user_reviews(self):
        reviews_section = self.user_page.find(href='/user/{}'.format(self.username)+'/reviews/')
        reviews =  reviews_section.find(class_='profileStat').getText()
        reviews_JSON = {
            "reviews" : reviews
        }
        return json.dumps(reviews_JSON)

    def get_user_lists(self):
        lists_section = self.user_page.find(href='/user/{}'.format(self.username)+'/lists/')
        lists =  lists_section.find(class_='profileStat').getText()
        lists_JSON = {
            "lists" : lists
        }
        return json.dumps(lists_JSON)

    def get_user_followers(self):
        followers_section = self.user_page.find(href='/user/{}'.format(self.username)+'/followers/')
        followers =  followers_section.find(class_='profileStat').getText()
        followers_JSON = {
            "followers" : followers
        }
        return json.dumps(followers_JSON)

    def get_user_about(self):
        about_user =  self.user_page.find(class_='aboutUser').getText()
        about_user_JSON = {
            "about_user" : about_user
        }
        return json.dumps(about_user_JSON)