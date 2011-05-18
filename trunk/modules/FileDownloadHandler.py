from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

import os

class FileDownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, file_id):
    file_info = FileInfo.get_by_id(long(file_id))
    if not file_info or not file_info.blob:
      self.error(404)
      return
    self.send_blob(file_info.blob, save_as=True)