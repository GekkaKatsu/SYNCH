from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from models.UserModel import User
from modules.CryptographicHash import md5HashSum

"""
Adding exceptions
"""
from modules.exceptions.RegisterExceptions import EmailIsAlreadyRegistred

class RegisterHandler(webapp.RequestHandler):
    def get(self):
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("user/register.html",templateArguments))
    def post(self):
         user = User()
         user.FirstName = self.request.get('firstname')
         user.LastName = self.request.get('lastname')
         user.Mail = self.request.get('email')
         user.Password = str(md5HashSum().valueToHash(self.request.get('password')))    
         
         try:            
             user.put()
         except EmailIsAlreadyRegistred,e:
             self.response.out.write( 'Email: ' + e.__str__() + ' already registred..')
             return; 
                  
         self.response.out.write('Succesfully Registred:' + user.FirstName + " " + user.LastName)