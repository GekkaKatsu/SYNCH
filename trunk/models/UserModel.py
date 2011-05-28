from google.appengine.ext import db
from google.appengine.api import users
from modules.exceptions.RegisterExceptions import EmailIsAlreadyRegistred

class User(db.Model):
    FirstName = db.StringProperty()
    LastName = db.StringProperty()
    Mail = db.StringProperty()
    Password = db.StringProperty()
    CreationDate = db.DateTimeProperty (auto_now_add=True)
    
    def put (self):
     # Make sure e-mails are unique for each user     
     if (not self.is_saved()) and (db.GqlQuery("SELECT * FROM User WHERE Mail = :1",self.Mail).count() > 0):
         raise EmailIsAlreadyRegistred ( self.Mail ) 
     # call the parent method
     db.Model.put (self)

