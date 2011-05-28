
class EmailIsAlreadyRegistred (Exception):
    def __init__(self,  alreadyRegistredEmail):
         self.alreadyRegistredEmail = alreadyRegistredEmail
    def __str__(self):
         return str(self.alreadyRegistredEmail)  