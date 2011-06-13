from google.appengine.ext import db

from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class FileInfo(db.Model):
  blob = blobstore.BlobReferenceProperty(required=True)
  uploaded_by = db.StringProperty(required=True)
  uploaded_at = db.DateTimeProperty(required=True, auto_now_add=True)