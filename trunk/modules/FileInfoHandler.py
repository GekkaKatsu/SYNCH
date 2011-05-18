from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

import os
from modules.BaseHandler import BaseHandler

class FileInfoHandler(BaseHandler):
  def get(self, file_id):
    file_info = FileInfo.get_by_id(long(file_id))
    if not file_info:
      self.error(404)
      return
    self.render_template("info.html", {
        'file_info': file_info,
        'logout_url': users.create_logout_url('/'),
    })