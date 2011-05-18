from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

import os
from modules.BaseHandler import BaseHandler

class FileUploadFormHandler(BaseHandler):
  def get(self):
    self.render_template("upload.html", {
        'form_url': blobstore.create_upload_url('/upload'),
        'logout_url': users.create_logout_url('/'),
    })