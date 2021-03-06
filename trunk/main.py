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

from handlers.MainHandler import MainHandler
from handlers.LoginHandler import LoginHandler
from handlers.RegisterHandler import RegisterHandler
from handlers.UserProfileHandler import UserProfileHandler
from handlers.WebFileInfoHandler import FileInfoHandler
from handlers.WebFrontendUploadHandler import WebFrontendUploadHandler
from handlers.WebDataUploadHandler import FileUploadHandler

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                         ('/login', LoginHandler),
                                         ('/register', RegisterHandler),
                                         ('/userprofile', UserProfileHandler),
                                         ('/fileupload',WebFrontendUploadHandler),
                                         ('/upload',FileUploadHandler),
                                         ('/file/([0-9]+)',FileInfoHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
