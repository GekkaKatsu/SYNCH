#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db

class IpLog(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)


class MainHandler(webapp.RequestHandler):
    def get(self):
        if self.request.get('katsu'):            
            self.response.out.write('<b>' + self.request.get('katsu') + '</b>')
            x = self.request.get('katsu')
            if x != Logger().entries[-1]:
                self.response.out.write('<b> OK</b>')
                
            else:
                self.response.out.write('<b> Already in list</b>')
        elif self.request.get('mode') == 'view':
            try:
                for entry in Logger().entries:
                    self.response.out.write('<b>' + entry + '</b><br>')
            except Exception as e:
                self.response.out.write('<b>Error..</b><br>')
        else:
            self.response.out.write('<b>' + "Invalid Try..Faggot" + '</b>')
        
        


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
