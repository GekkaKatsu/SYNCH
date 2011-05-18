from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os

class BaseHandler(webapp.RequestHandler):
  def render_template(self, file, template_args):
    self.response.out.write(file)
    try:
        path = os.path.join(os.path.dirname(__file__), "../templates", file)
    except Exception,e:
        self.response.out.write(path)
    self.response.out.write(path)
    self.response.out.write(template.render(path, template_args))

