from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.decorators.loginDecorator import loginRequired

from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class WebFrontendUploadHandler(webapp.RequestHandler):
  @loginRequired
  def get(self):
        arguments =     {
        'form_url': blobstore.create_upload_url('/upload')
                    }
        self.response.out.write(RenderTemplate("upload/upload.html",arguments))
