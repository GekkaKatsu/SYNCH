from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate

class MainHandler(webapp.RequestHandler):
    def get(self):
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("index.html",templateArguments))