import os
from google.appengine.ext.webapp import template

def RenderTemplate(path,template_value):
    path = os.path.join("templates",path)
    rendredTemplate = template.render(path,template_value)
    return rendredTemplate