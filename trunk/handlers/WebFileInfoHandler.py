from google.appengine.ext import webapp
from modules.TemplateRender import RenderTemplate
from modules.decorators.loginDecorator import loginRequired

from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from models.FileInfo import FileInfo

from modules.BaseFileInfoFields import BaseFileInfoFields

class FileInfoHandler(webapp.RequestHandler):
  @loginRequired
  def get(self, file_id):
    fileInfoRef = FileInfo.get_by_id(long(file_id))
        
    if not fileInfoRef:
        self.error(404)
        return
    fileinfo = BaseFileInfoFields( fileInfoRef )    
    metafileinfocolumns = {'meta information 1:': 'wide - 16', 'meta information 2:': 'wide - 32'}
      
    self.response.out.write(RenderTemplate("file/info.html", {
        'fileinfocolumns': fileinfo,
        'metafileinfocolumns' : metafileinfocolumns
    }))