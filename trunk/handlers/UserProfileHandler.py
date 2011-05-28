from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate

class UserProfileHandler(webapp.RequestHandler):
    def get(self):
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("user/profile.html",templateArguments))