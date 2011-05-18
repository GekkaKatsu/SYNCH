from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

import os

class FileUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    blob_info = self.get_uploads()[0]
    if not users.get_current_user():
      blob_info.delete()
      self.redirect(users.create_login_url("/"))
      return

    file_info = FileInfo(blob=blob_info.key(),
                         uploaded_by=users.get_current_user())
    db.put(file_info)
    self.redirect("/file/%d" % (file_info.key().id(),))