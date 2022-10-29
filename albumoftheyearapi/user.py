from asyncio.windows_events import NULL
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

<<<<<<< HEAD
class UserMethods():
    """ Methods for gettting a user's profile data """
=======
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

class UserMethods:
    def __init__(self):
<<<<<<< HEAD
        self.user = ''
        self.url = ''

    def __set_user_page(self, user, url):
        print( 'Making a request' )
        self.user = user
        self.url = url
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/6.0'})
=======
        self.user = ""

    def __set_user_page(self, user):
        print("Making a request")
        self.user = user
        self.url = "https://www.albumoftheyear.org/user/{}".format(user)
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        ugly_user_page = urlopen(self.req).read()
        self.user_page = BeautifulSoup(ugly_user_page, "html.parser")

<<<<<<< HEAD
    def user_rating_count(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)
          
        ratings_section = self.user_page.find(href='/user/{}'.format(self.user)+'/ratings/')
        ratings =  ratings_section.find(class_='profileStat').getText()
=======
    def __get_user_rating_count(self, user):
        if self.user != user:
            self.__set_user_page(user)

        ratings_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/ratings/"
        )
        ratings = ratings_section.find(class_="profileStat").getText()
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return ratings

    def user_rating_count_json(self, user):
<<<<<<< HEAD
        ratings_JSON = {
            "ratings": self.user_rating_count(user)
        }
=======
        ratings_JSON = {"ratings": self.__get_user_rating_count(user)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(ratings_JSON)

    def user_review_count(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)

        reviews_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/reviews/"
        )
        reviews = reviews_section.find(class_="profileStat").getText()
        return reviews
<<<<<<< HEAD
    
    def user_review_count_json(self, user):
        reviews_JSON = {
            "reviews": self.user_review_count(user)
        }
=======

    def user_review_count(self, user):
        return self.__get_user_review_count(user)

    def get_review_count_json(self, user):
        reviews_JSON = {"reviews": self.__get_user_review_count(user)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(reviews_JSON)

    def user_list_count(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)

        lists_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/lists/"
        )
        lists = lists_section.find(class_="profileStat").getText()
        return lists

<<<<<<< HEAD
    def user_list_count_json(self, user):
        lists_JSON = {
            "lists": self.user_list_count(user)
        }
=======
    def user_list_count(self, user):
        return self.__get_user_list_count(user)

    def user_lists_json(self, user):
        lists_JSON = {"lists": self.__get_user_list_count(user)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(lists_JSON)

    def user_follower_count(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)

        followers_section = self.user_page.find(
            href="/user/{}".format(self.user) + "/followers/"
        )
        followers = followers_section.find(class_="profileStat").getText()
        return followers

    def user_follower_count_json(self, user):
<<<<<<< HEAD
        followers_JSON = {
            "followers": self.user_follower_count(user)
        }
=======
        followers_JSON = {"followers": self.__get_user_follower_count(user)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(followers_JSON)

    def user_about(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)

        about = self.user_page.find(class_="aboutUser").getText()
        return about

    def user_about_json(self, user):
<<<<<<< HEAD
        about_JSON = {
            "about_user": self.user_about(user)
        }
=======
        about_JSON = {"about_user": self.__get_user_about(user)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(about_JSON)

    def user_rating_distribution(self, user):
        url = self.user_url+user
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
            "100"   : user_rating_distribution[0],
            "90-99" : user_rating_distribution[1],
            "80-89" : user_rating_distribution[2],
            "70-79" : user_rating_distribution[3],
            "60-69" : user_rating_distribution[4],
            "50-59" : user_rating_distribution[5],
            "40-49" : user_rating_distribution[6],
            "30-39" : user_rating_distribution[7],
            "20-29" : user_rating_distribution[8],
            "10-19" : user_rating_distribution[9],
            "0-9"   : user_rating_distribution[10]
        }

<<<<<<< HEAD
        return json.dumps(user_rating_distribution_JSON)

    def user_ratings(self, user):
        url = self.user_url+user
        if self.url != url:
            self.__set_user_page(user, url)
          
        return self.user_page.find(class_='albumBlock').getText()

    def user_ratings_json(self, user):
        ratings_JSON = {
            "ratings": self.user_ratings(user)
=======
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
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        }
        return json.dumps(ratings_JSON)

    def user_perfect_scores(self, user):
        """ Returns a list of the users perfect scores """

<<<<<<< HEAD
        url = self.user_url+user+'/ratings/perfect/'
        if self.url != url:
            self.__set_user_page(user, url)
          
        perfect_scores = self.user_page.find(class_='albumBlock')
        if perfect_scores == None:
            return ""
        return perfect_scores.getText()

    def user_perfect_scores_json(self, user):
        """ Returns a list of the users perfect scores in JSON format """

        perfect_sccores_json = {
            "perfect scores": self.user_perfect_scores(user)
        }
        return json.dumps(perfect_sccores_json)

    def user_liked_music(self, user):
        """ Returns a list of the users liked music """

        url = self.user_url+user+'/liked/albums/'
        if self.url != url:
            self.__set_user_page(user, url)

        liked_music = self.user_page.find_all(class_='albumBlock')

        result = []
        for entry in liked_music:
            artist = entry.find(class_='artistTitle').getText().encode('ascii', 'ignore').decode() # Gets rid of weird characters
            album = entry.find(class_='albumTitle').getText().encode('ascii', 'ignore').decode()
            combined = artist +': ' +album
            result.append(combined)

        return result

    def user_liked_music_json(self, user):
        """ Returns a list of the users liked music in JSON format """

        liked_music_json = {
            "liked music": self.user_liked_music(user)
        }
        return json.dumps(liked_music_json)
=======
        return json.dumps(user_rating_distribution_JSON)
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
