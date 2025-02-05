import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class ArtistMethods:
    """Initializes all methods that are used to get user data"""

    def __init__(self):
        self.artist = ""
        self.url = ""
        self.artist_url = "https://www.albumoftheyear.org/artist/"
        
        self.albums = []

    def __set_artist_page(self, artist, url):
        self.artist = artist
        self.url = url
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
        ugly_artist_page = urlopen(self.req).read()
        self.artist_page = BeautifulSoup(ugly_artist_page, "html.parser")
        self.__get_discography(artist)
        self.__get_community_data(artist)

    def __class_text(self, artist, class_name, url):
        if self.url != url:
            self.__set_artist_page(artist, url)

        return self.artist_page.find(class_=class_name).getText()
    
    def __get_discography(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)

        # Dictionary to store albums under their respective categories
        categorized_albums = {}

        # Find all h2 and div elements inside the artist page
        elements = self.artist_page.find_all(["h2", "div"])
        current_category = None  # To track which category the divs belong to

        for element in elements:
            if element.name == "h2":
                # New category found, update current_category
                current_category = element.get_text(strip=True)
                categorized_albums[current_category] = []  # Initialize list for this category
            elif element.name == "div" and current_category == "Similar Artists":
                # Similar Artists is structured differently
                album_title_div = element.find("div", class_="name")
                if album_title_div:
                    album_name = album_title_div.get_text().encode("ascii", "ignore").decode().strip()
                    categorized_albums[current_category].append(album_name)
            elif element.name == "div" and current_category:
                # For each category, loop through all divs to find the album title
                album_title_div = element.find("div", class_="albumTitle")
                if album_title_div:
                    album_name = album_title_div.get_text().encode("ascii", "ignore").decode().strip()
                    categorized_albums[current_category].append(album_name)
                
        self.albums = categorized_albums['Albums']
        self.mixtapes = categorized_albums['Mixtapes']
        self.eps = categorized_albums['EPs']
        # self.live_albums = categorized_albums['Live Albums'] # UNUSED
        # self.compilations = categorized_albums['Compilations'] # UNUSED
        self.singles = categorized_albums['SinglesView All']
        # self.appears_on = categorized_albums['Appears OnView All'] # UNUSED
        self.similar_artists_cat = categorized_albums['Similar Artists']

    def __get_community_data(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)

        # Find all <tr> elements
        rows = self.artist_page.find_all("tr")

        extracted_texts = []  # Store extracted text from <a> elements

        for row in rows:
            # Find the div with class "songAlbum" inside this row
            song_album_div = row.find("td", class_="songAlbum")
        
            if song_album_div:
                # Find the <a> tag inside this div
                link = song_album_div.find("a")
                if link:
                    text = link.get_text().strip()
                    extracted_texts.append(text)

        self.top_songs = extracted_texts

    def artist_albums(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
            
        return self.albums

    def artist_albums_json(self, artist):
        albums_JSON = {"albums": self.artist_albums(artist)}
        return json.dumps(albums_JSON)

    def artist_mixtapes(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
            
        return self.mixtapes

    def artist_mixtapes_json(self, artist):
        mixtapes_JSON = {"mixtapes": self.artist_mixtapes(artist)}
        return json.dumps(mixtapes_JSON)

    def artist_eps(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
            
        return self.eps

    def artist_eps_json(self, artist):
        eps_JSON = {"eps": self.artist_eps(artist)}
        return json.dumps(eps_JSON)

    def artist_singles(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
        
        return self.singles

    def artist_singles_json(self, artist):
        singles_JSON = {"singles": self.artist_singles(artist)}
        return json.dumps(singles_JSON)

    def artist_name(self, artist):
        return self.__class_text(
            artist, "artistHeadline", self.artist_url + artist + "/"
        )

    def artist_name_json(self, artist):
        name_JSON = {"name": self.artist_name(artist)}
        return json.dumps(name_JSON)

    def artist_critic_score(self, artist):
        return self.__class_text(
            artist, "artistCriticScore", self.artist_url + artist + "/"
        )

    def artist_critic_score_json(self, artist):
        critic_score_JSON = {"critic score": self.artist_critic_score(artist)}
        return json.dumps(critic_score_JSON)

    def artist_user_score(self, artist):
        return self.__class_text(
            artist, "artistUserScore", self.artist_url + artist + "/"
        )

    def artist_user_score_json(self, artist):
        user_score_JSON = {"user score": self.artist_user_score(artist)}
        return json.dumps(user_score_JSON)

    def artist_total_score(self, artist):
        return (
            int(self.artist_critic_score(artist)) + int(self.artist_user_score(artist))
        ) / 2

    def artist_total_score_json(self, artist):
        total_score_JSON = {"total score": self.artist_total_score(artist)}
        return json.dumps(total_score_JSON)

    def artist_follower_count(self, artist):
        return self.__class_text(artist, "followCount", self.artist_url + artist + "/")

    def artist_follower_count_json(self, artist):
        follower_count_JSON = {"follower count": self.artist_follower_count(artist)}
        return json.dumps(follower_count_JSON)

    def artist_details(self, artist):
        return self.__class_text(
            artist, "artistTopBox info", self.artist_url + artist + "/"
        )

    def artist_details_json(self, artist):
        artist_details_JSON = {"artist details": self.artist_details(artist)}
        return json.dumps(artist_details_JSON)

    def artist_top_songs(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
            
        return self.top_songs

    def artist_top_songs_json(self, artist):
        artist_top_songs_JSON = {"top songs": self.artist_top_songs(artist)}
        return json.dumps(artist_top_songs_JSON)

    def similar_artists(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
            
        return self.similar_artists_cat

    def similar_artists_json(self, artist):
        similar_artists_JSON = {"similar artists": self.similar_artists(artist)}
        return json.dumps(similar_artists_JSON)
