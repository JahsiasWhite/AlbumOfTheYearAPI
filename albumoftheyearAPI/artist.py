
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

class ArtistMethods:

    def __init__(self):
        self.artist = ''

    def __set_artist_page(self, artist):
        print( 'Making a request' )
        self.artist = artist
        self.url = 'https://www.albumoftheyear.org/artist/{}'.format(artist)+'/'
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/6.0'})
        ugly_artist_page = urlopen(self.req).read()
        self.artist_page = BeautifulSoup(ugly_artist_page, 'html.parser')

    def __class_text(self, id, class_name):
        if self.artist != id:
            self.__set_user_page(id)

          
        return self.artist_page.find(class_=class_name).getText()

    def __get_artist_albums(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)
          
        albums = self.artist_page.find_all(attrs={"data-type":'lp'})

        artist_albums = []
        for x in albums:
            album = x.getText().encode('ascii', 'ignore').decode()[4:]
            album_name = album.split('LP')[0]
            artist_albums.append(album_name)

        return artist_albums

    def artist_albums(self, artist):
        return self.__get_artist_albums(artist)

    def artist_albums_json(self, artist):
        albums_JSON = {
            "albums": self.__get_artist_albums(artist)
        }
        return json.dumps(albums_JSON)

    def __get_artist_mixtapes(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)
          
        mixtapes = self.artist_page.find_all(attrs={"data-type":'mixtape'})

        artist_mixtapes = []
        for x in mixtapes:
            mixtape = x.getText().encode('ascii', 'ignore').decode()[4:]
            mixtape_name = mixtape.split('Mixtape')[0]
            artist_mixtapes.append(mixtape_name)

        return artist_mixtapes

    def artist_mixtapes(self, artist):
        return self.__get_artist_mixtapes(artist)

    def artist_mixtapes_json(self, artist):
        mixtapes_JSON = {
            "mixtapes": self.__get_artist_mixtapes(artist)
        }
        return json.dumps(mixtapes_JSON)

    def __get_artist_eps(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)
          
        eps = self.artist_page.find_all(attrs={"data-type":'ep'})

        artist_eps = []
        for x in eps:
            ep = x.getText().encode('ascii', 'ignore').decode()[4:]
            ep_name = ep.split('EP')[0]
            artist_eps.append(ep_name)

        return artist_eps

    def artist_eps(self, artist):
        return self.__get_artist_eps(artist)

    def artist_eps_json(self, artist):
        eps_JSON = {
            "eps": self.__get_artist_eps(artist)
        }
        return json.dumps(eps_JSON)

    def __get_artist_singles(self, artist):
        if self.artist != artist:
            self.__set_artist_page(artist)
          
        singles = self.artist_page.find_all(attrs={"data-type":'single'})

        artist_singles = []
        for x in singles:
            single = x.getText().encode('ascii', 'ignore').decode()[4:]
            single_name = single.split('Single')[0]
            artist_singles.append(single_name)

        return artist_singles

    def artist_singles(self, artist):
        return self.__get_artist_singles(artist)

    def artist_singles_json(self, artist):
        singles_JSON = {
            "singles": self.__get_artist_singles(artist)
        }
        return json.dumps(singles_JSON)

    def __get_artist_name(self, artist):
        return self.__class_text(artist, 'artistHeadline')

    def artist_name(self, artist):
        return self.__get_artist_name(artist)

    def artist_name_json(self, artist):
        name_JSON = {
            "name": self.__get_artist_name(artist)
        }
        return json.dumps(name_JSON)

    def __get_artist_critic_score(self, artist):
        return self.__class_text(artist, 'artistCriticScore')

    def artist_critic_score(self, artist):
        return self.__get_artist_critic_score(artist)

    def artist_critic_score_json(self, artist):
        critic_score_JSON = {
            "critic score": self.__get_artist_critic_score(artist)
        }
        return json.dumps(critic_score_JSON)

    def __get_artist_user_score(self, artist):
        return self.__class_text(artist, 'artistUserScore')

    def artist_user_score(self, artist):
        return self.__get_artist_user_score(artist)

    def artist_user_score_json(self, artist):
        user_score_JSON = {
            "user score": self.__get_artist_user_score(artist)
        }
        return json.dumps(user_score_JSON)

    def __get_artist_total_score(self, artist):
        return self.artist_critic_score(artist) + self.artist_user_score(artist)

    def artist_total_score(self, artist):
        return self.__get_artist_total_score(artist)

    def artist_total_score_json(self, artist):
        total_score_JSON = {
            "total score": self.__get_artist_total_score(artist)
        }
        return json.dumps(total_score_JSON)

    def __get_artist_follower_count(self, artist):
        return self.__class_text(artist, 'followCount')

    def artist_follower_count(self, artist):
        return self.__get_artist_follower_count(artist)

    def artist_follower_count_json(self, artist):
        follower_count_JSON = {
            "follower count": self.__get_artist_follower_count(artist)
        }
        return json.dumps(follower_count_JSON)
    
    def __get_artist_details(self, artist):
        return self.__class_text(artist, 'artistTopBox info')

    def artist_details(self, artist):
        return self.__get_artist_details(artist)

    def artist_details_json(self, artist):
        artist_details_JSON = {
            "artist details": self.__get_artist_details(artist)
        }
        return json.dumps(artist_details_JSON)

    def __get_artist_top_songs(self, artist):
        return self.__class_text(artist, 'trackListTable')

    def artist_top_songs(self, artist):
        return self.__get_artist_top_songs(artist)

    def artist_top_songs_json(self, artist):
        artist_top_songs_JSON = {
            "top songs": self.__get_artist_top_songs(artist)
        }
        return json.dumps(artist_top_songs_JSON)

    def __get_similar_artists(self, artist):
        return self.__class_text(artist, 'section relatedArtists')

    def similar_artists(self, artist):
        return self.__get_similar_artists(artist)

    def similar_artists_json(self, artist):
        similar_artists_JSON = {
            "similar artists": self.__get_similar_artists(artist)
        }
        return json.dumps(similar_artists_JSON)