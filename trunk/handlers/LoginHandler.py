from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.CryptographicHash import md5HashSum
from modules.appengine_utilities.sessions import Session
from google.appengine.ext import db

from modules.exceptions.AuthExceptions import BadAuth

class LoginHandler(webapp.RequestHandler):
    def get(self):
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("user/login.html",templateArguments))
    def post(self):
        templateArguments = ""
        email = self.request.get('email')
        password = self.request.get('password')
        try:
            if db.GqlQuery("SELECT * FROM User WHERE Mail = :1",email).count() > 0:
                userPasswordHash = db.GqlQuery("SELECT * FROM User WHERE Mail = :1",email).get().Password
                if userPasswordHash == md5HashSum().valueToHash(password):                
                    session = Session()
                    session['email'] = email
                    self.redirect("/userprofile");
                else:
                    raise BadAuth(email)
            else:
                raise BadAuth(email)
        except BadAuth, e:
                templateArguments = { 'Email': e.__str__() }
                self.response.out.write(RenderTemplate("exceptions/badauth.html",templateArguments))
            
                
                