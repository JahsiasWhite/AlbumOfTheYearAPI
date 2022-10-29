<<<<<<< HEAD
import json
=======
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

<<<<<<< HEAD
class ArtistMethods:
    """ Initializes all methods that are used to get user data """
=======
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

class ArtistMethods:
    def __init__(self):
<<<<<<< HEAD
        self.artist = ''
        self.url = ''

    def __set_artist_page(self, artist, url):
        print( 'Getting Artist Info' )
        self.artist = artist
        self.url = url
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/6.0'})
=======
        self.artist = ""

    def __set_artist_page(self, artist):
        print("Making a request")
        self.artist = artist
        self.url = "https://www.albumoftheyear.org/artist/{}".format(artist) + "/"
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        ugly_artist_page = urlopen(self.req).read()
        self.artist_page = BeautifulSoup(ugly_artist_page, "html.parser")

<<<<<<< HEAD
    def __class_text(self, artist, class_name, url):
        if self.url != url:
            self.__set_user_page(artist, url)
          
        return self.artist_page.find(class_=class_name).getText()

    def artist_albums(self, artist):
        url = self.artist_url+artist+'/'
        if self.url != url:
            self.__set_artist_page(artist, url)
          
        albums = self.artist_page.find_all(attrs={"data-type":'lp'})
=======
    def __class_text(self, id, class_name):
        if self.artist != id:
            self.__set_user_page(id)

        return self.artist_page.find(class_=class_name).getText()

    def __get_artist_albums(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)

        albums = self.artist_page.find_all(attrs={"data-type": "lp"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

        artist_albums = []
        for x in albums:
            album = x.getText().encode("ascii", "ignore").decode()[4:]
            album_name = album.split("LP")[0]
            artist_albums.append(album_name)

        return artist_albums

    def artist_albums_json(self, artist):
<<<<<<< HEAD
        albums_JSON = {
            "albums": self.artist_albums(artist)
        }
        return json.dumps(albums_JSON)

    def artist_mixtapes(self, artist):
        url = self.artist_url+artist+'/'
        if self.url != url:
            self.__set_artist_page(artist, url)
          
        mixtapes = self.artist_page.find_all(attrs={"data-type":'mixtape'})
=======
        albums_JSON = {"albums": self.__get_artist_albums(artist)}
        return json.dumps(albums_JSON)

    def __get_artist_mixtapes(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)

        mixtapes = self.artist_page.find_all(attrs={"data-type": "mixtape"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

        artist_mixtapes = []
        for x in mixtapes:
            mixtape = x.getText().encode("ascii", "ignore").decode()[4:]
            mixtape_name = mixtape.split("Mixtape")[0]
            artist_mixtapes.append(mixtape_name)

        return artist_mixtapes

    def artist_mixtapes_json(self, artist):
<<<<<<< HEAD
        mixtapes_JSON = {
            "mixtapes": self.artist_mixtapes(artist)
        }
        return json.dumps(mixtapes_JSON)

    def artist_eps(self, artist):
        url = self.artist_url+artist+'/'
        if self.url != url:
            self.__set_artist_page(artist, url)
          
        eps = self.artist_page.find_all(attrs={"data-type":'ep'})
=======
        mixtapes_JSON = {"mixtapes": self.__get_artist_mixtapes(artist)}
        return json.dumps(mixtapes_JSON)

    def __get_artist_eps(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)

        eps = self.artist_page.find_all(attrs={"data-type": "ep"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

        artist_eps = []
        for x in eps:
            ep = x.getText().encode("ascii", "ignore").decode()[4:]
            ep_name = ep.split("EP")[0]
            artist_eps.append(ep_name)

        return artist_eps

    def artist_eps_json(self, artist):
<<<<<<< HEAD
        eps_JSON = {
            "eps": self.artist_eps(artist)
        }
        return json.dumps(eps_JSON)

    def artist_singles(self, artist):
        url = self.artist_url+artist+'/'
        if self.url != url:
            self.__set_artist_page(artist, url)
        singles = self.artist_page.find_all(attrs={"data-type":'single'})
=======
        eps_JSON = {"eps": self.__get_artist_eps(artist)}
        return json.dumps(eps_JSON)

    def __get_artist_singles(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)

        singles = self.artist_page.find_all(attrs={"data-type": "single"})
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

        artist_singles = []
        for x in singles:
            single = x.getText().encode("ascii", "ignore").decode()[4:]
            single_name = single.split("Single")[0]
            artist_singles.append(single_name)

        return artist_singles

    def artist_singles_json(self, artist):
<<<<<<< HEAD
        singles_JSON = {
            "singles": self.artist_singles(artist)
        }
        return json.dumps(singles_JSON)

=======
        singles_JSON = {"singles": self.__get_artist_singles(artist)}
        return json.dumps(singles_JSON)

    def __get_artist_name(self, artist):
        return self.__class_text(artist, "artistHeadline")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def artist_name(self, artist):
        return self.__class_text(artist, 'artistHeadline', self.artist_url+artist+'/')

    def artist_name_json(self, artist):
<<<<<<< HEAD
        name_JSON = {
            "name": self.artist_name(artist)
        }
        return json.dumps(name_JSON)

=======
        name_JSON = {"name": self.__get_artist_name(artist)}
        return json.dumps(name_JSON)

    def __get_artist_critic_score(self, artist):
        return self.__class_text(artist, "artistCriticScore")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def artist_critic_score(self, artist):
        return self.__class_text(artist, 'artistCriticScore', self.artist_url+artist+'/')

    def artist_critic_score_json(self, artist):
<<<<<<< HEAD
        critic_score_JSON = {
            "critic score": self.artist_critic_score(artist)
        }
        return json.dumps(critic_score_JSON)

=======
        critic_score_JSON = {"critic score": self.__get_artist_critic_score(artist)}
        return json.dumps(critic_score_JSON)

    def __get_artist_user_score(self, artist):
        return self.__class_text(artist, "artistUserScore")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def artist_user_score(self, artist):
        return self.__class_text(artist, 'artistUserScore', self.artist_url+artist+'/')

    def artist_user_score_json(self, artist):
<<<<<<< HEAD
        user_score_JSON = {
            "user score": self.artist_user_score(artist)
        }
=======
        user_score_JSON = {"user score": self.__get_artist_user_score(artist)}
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
        return json.dumps(user_score_JSON)

    def artist_total_score(self, artist):
        return (int(self.artist_critic_score(artist)) + int(self.artist_user_score(artist))) / 2

    def artist_total_score_json(self, artist):
<<<<<<< HEAD
        total_score_JSON = {
            "total score": self.artist_total_score(artist)
        }
        return json.dumps(total_score_JSON)

=======
        total_score_JSON = {"total score": self.__get_artist_total_score(artist)}
        return json.dumps(total_score_JSON)

    def __get_artist_follower_count(self, artist):
        return self.__class_text(artist, "followCount")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def artist_follower_count(self, artist):
        return self.__class_text(artist, 'followCount', self.artist_url+artist+'/')

    def artist_follower_count_json(self, artist):
        follower_count_JSON = {
            "follower count": self.artist_follower_count(artist)
        }
        return json.dumps(follower_count_JSON)
<<<<<<< HEAD
=======

    def __get_artist_details(self, artist):
        return self.__class_text(artist, "artistTopBox info")
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4

    def artist_details(self, artist):
        return self.__class_text(artist, 'artistTopBox info', self.artist_url+artist+'/')

    def artist_details_json(self, artist):
<<<<<<< HEAD
        artist_details_JSON = {
            "artist details": self.artist_details(artist)
        }
        return json.dumps(artist_details_JSON)

=======
        artist_details_JSON = {"artist details": self.__get_artist_details(artist)}
        return json.dumps(artist_details_JSON)

    def __get_artist_top_songs(self, artist):
        return self.__class_text(artist, "trackListTable")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def artist_top_songs(self, artist):
        return self.__class_text(artist, 'trackListTable', self.artist_url+artist+'/')

    def artist_top_songs_json(self, artist):
<<<<<<< HEAD
        artist_top_songs_JSON = {
            "top songs": self.artist_top_songs(artist)
        }
        return json.dumps(artist_top_songs_JSON)

=======
        artist_top_songs_JSON = {"top songs": self.__get_artist_top_songs(artist)}
        return json.dumps(artist_top_songs_JSON)

    def __get_similar_artists(self, artist):
        return self.__class_text(artist, "section relatedArtists")

>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
    def similar_artists(self, artist):
        return self.__class_text(artist, 'section relatedArtists', self.artist_url+artist+'/')

    def similar_artists_json(self, artist):
<<<<<<< HEAD
        similar_artists_JSON = {
            "similar artists": self.similar_artists(artist)
        }
        return json.dumps(similar_artists_JSON)
=======
        similar_artists_JSON = {"similar artists": self.__get_similar_artists(artist)}
        return json.dumps(similar_artists_JSON)
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
