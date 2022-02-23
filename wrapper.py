
#import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class User(object):

    def __init__(self, user):
        req = Request('https://www.albumoftheyear.org/user/{}'.format(user), headers={'User-Agent': 'Mozilla/6.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    #def getUser(self, user):
        

    def getUserRatings(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/ratings/')
        ratings =  obj.find(class_='profileStat').getText()
        return ratings
    
    def getUserReviews(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/reviews/')
        reviews =  obj.find(class_='profileStat').getText()
        return reviews

    def getUserLists(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/lists/')
        Lists =  obj.find(class_='profileStat').getText()
        return Lists

    def getUserFollowers(self, user, soup):
        obj = soup.find(href='/user/{}'.format(user)+'/followers/')
        Followers =  obj.find(class_='profileStat').getText()
        return Followers

    def getUserAbout(self, user, soup):
        aboutUser =  soup.find(class_='aboutUser').getText()
        return aboutUser
