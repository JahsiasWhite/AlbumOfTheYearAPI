
from albumoftheyearAPI.user import UserMethods
from albumoftheyearAPI.artist import ArtistMethods

class AOTY(UserMethods, ArtistMethods):
    
    def __init__(self):
        self.user = ''
        self.artist = ''