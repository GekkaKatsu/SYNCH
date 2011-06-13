from modules.appengine_utilities.sessions import Session

def loginRequired(func):
  def wrapper(self, *args, **kw):
    self.sess = Session()
    try:
        user = self.sess['email']
    except KeyError:        
        self.redirect("/login")
        return wrapper
    func(self, *args, **kw)
  return wrapper