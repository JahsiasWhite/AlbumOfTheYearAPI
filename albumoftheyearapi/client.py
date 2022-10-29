<<<<<<< HEAD
""" All methods used to get site data """
=======
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
from albumoftheyearapi.user import UserMethods
from albumoftheyearapi.artist import ArtistMethods


class AOTY(UserMethods, ArtistMethods):
<<<<<<< HEAD
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
=======
    def __init__(self):
        self.user = ""
        self.artist = ""
>>>>>>> dec7777d24ad6d11d703fd1225d95ba8628a75d4
