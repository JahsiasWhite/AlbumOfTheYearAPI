
#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


class User(object):

    def getUserPage(self, user):
        req = Request('https://www.albumoftheyear.org/user/{}'.format(user), headers={'User-Agent': 'Mozilla/6.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def getUserRatings(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/ratings/')
        ratings =  obj.find(class_='profileStat').getText()
        ratings_JSON = {
            "ratings" : ratings
        }
        return json.dumps(ratings_JSON)
    
    def getUserReviews(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/reviews/')
        reviews =  obj.find(class_='profileStat').getText()
        reviews_JSON = {
            "reviews" : reviews
        }
        return json.dumps(reviews_JSON)

    def getUserLists(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/lists/')
        lists =  obj.find(class_='profileStat').getText()
        lists_JSON = {
            "lists" : lists
        }
        return json.dumps(lists_JSON)

    def getUserFollowers(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/followers/')
        followers =  obj.find(class_='profileStat').getText()
        followers_JSON = {
            "followers" : followers
        }
        return json.dumps(followers_JSON)

    def getUserAbout(self, user, soup):
        about_user =  soup.find(class_='aboutUser').getText()
        about_user_JSON = {
            "about_user" : about_user
        }
        return json.dumps(about_user_JSON)
