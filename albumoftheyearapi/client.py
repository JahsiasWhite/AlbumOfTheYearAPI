""" All methods used to get site data """
from albumoftheyearapi.user import UserMethods
from albumoftheyearapi.artist import ArtistMethods

class AOTY(UserMethods, ArtistMethods):
    """ A light weight python library that acts as an API for https://www.albumoftheyear.org """

    def __init__(self):
        """ Initializes the required variables for getting website data.
    Required for easier caching
    """
        self.user = ''
        self.artist = ''
        self.url = ''
        self.user_url = 'https://www.albumoftheyear.org/user/'
        self.artist_url = 'https://www.albumoftheyear.org/artist/'
