from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.decorators.loginDecorator import loginRequired
from models.FileInfo import FileInfo

from models.FileInfo import FileInfo
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class FileUploadHandler(blobstore_handlers.BlobstoreUploadHandler):  
  @loginRequired
  def post(self):
    blob_info = self.get_uploads()[0]
    
    login = self.sess['email']

    file_info = FileInfo(blob=blob_info.key(),uploaded_by=login)
    db.put(file_info)
    self.redirect("/file/%d" % (file_info.key().id()))