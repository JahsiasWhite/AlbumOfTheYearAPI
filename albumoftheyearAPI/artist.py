
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

class ArtistMethods:

    def __init__(self):
        self = self

    def __set_artist_page(self, artist):
        print( 'Making a request' )
        self.artist = artist
        self.url = 'https://www.albumoftheyear.org/artist/{}'.format(artist)+'/'
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/6.0'})
        ugly_artist_page = urlopen(self.req).read()
        self.artist_page = BeautifulSoup(ugly_artist_page, 'html.parser')

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