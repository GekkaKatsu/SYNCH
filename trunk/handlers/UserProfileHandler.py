from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.decorators.loginDecorator import loginRequired
from modules.appengine_utilities.sessions import Session 
from google.appengine.ext import db

from models.FileInfo import FileInfo

from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class UserProfileHandler(webapp.RequestHandler):
    @loginRequired
    def get(self):        
        login = self.sess['email']
        
        files = FileInfo.all().filter('uploaded_by = ', login)        
        templateArguments = {'files':files }        
        self.response.out.write(RenderTemplate("user/profile.html",templateArguments))