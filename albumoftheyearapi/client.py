
from albumoftheyearapi.user import UserMethods
from albumoftheyearapi.artist import ArtistMethods

class AOTY(UserMethods, ArtistMethods):
    
    def __init__(self):
        self.user = ''
        self.artist = ''