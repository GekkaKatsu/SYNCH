

class BadAuth(Exception):
    def __init__(self,  BadAuthEmail):
         self.badAuthEmail = BadAuthEmail
    def __str__(self):
         return str(self.badAuthEmail)  
