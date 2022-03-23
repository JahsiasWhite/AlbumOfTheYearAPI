
from Client.user import UserMethods
from Client.artist import ArtistMethods

class Client(UserMethods, ArtistMethods):
    
    def __init__(self):
        self.user = ''
        self.artist = ''