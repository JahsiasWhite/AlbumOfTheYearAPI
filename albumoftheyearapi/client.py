""" All methods used to get site data """

from albumoftheyearapi.user import UserMethods
from albumoftheyearapi.artist import ArtistMethods
from albumoftheyearapi.album import AlbumMethods
from albumoftheyearapi.genre import GenreMethods
from albumoftheyearapi.ratings import RatingsMethods
from albumoftheyearapi.http import clear_cookies, set_cookies


class AOTY(UserMethods, ArtistMethods, AlbumMethods, GenreMethods, RatingsMethods):
    """A light weight python library that acts as an API for https://www.albumoftheyear.org"""

    def __init__(self, cookies=None, user_agent=None):
        """Initializes the required variables for getting website data.

        Args:
            cookies: optional Cloudflare/browser cookies as a dict or Cookie
                header string. Needed when albumoftheyear.org challenges bots.
            user_agent: User-Agent string that matches the browser those cookies
                came from (recommended when passing cf_clearance).
        """
        self.user = ""
        self.artist = ""
        self.url = ""
        self.user_url = "https://www.albumoftheyear.org/user/"
        self.artist_url = "https://www.albumoftheyear.org/artist/"
        self.upcoming_album_class = "albumBlock five small"
        self.aoty_albums_per_page = 60
        self.page_limit = 21
        # Genre stuff
        self.genre_base_url = "https://www.albumoftheyear.org/genre/"
        self.genre_page_url = ""
        self.genre_page = None
        # Ratings stuff
        self._ratings_page_url = ""
        self._ratings_page = None
        if cookies is not None or user_agent is not None:
            set_cookies(cookies=cookies, user_agent=user_agent)

    def set_cookies(self, cookies=None, user_agent=None, replace=True):
        """Update browser cookies used for albumoftheyear.org requests."""
        set_cookies(cookies=cookies, user_agent=user_agent, replace=replace)

    def clear_cookies(self):
        """Clear cookies previously set on this process."""
        clear_cookies()
