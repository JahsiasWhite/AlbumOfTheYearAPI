
from user import UserMethods

class Client(UserMethods):
    
    def __init__(self):
        self.user = ''

    def get(self):
        return self.get_user_ratings