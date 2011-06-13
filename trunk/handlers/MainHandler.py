from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.decorators.loginDecorator import loginRequired

class MainHandler(webapp.RequestHandler):
    @loginRequired
    def get(self):        
        templateArguments = "" #TODO
        self.response.out.write(RenderTemplate("index.html",templateArguments))