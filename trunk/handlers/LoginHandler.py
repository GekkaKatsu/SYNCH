from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate

class LoginHandler(webapp.RequestHandler):
    def get(self):
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("user/login.html",templateArguments))