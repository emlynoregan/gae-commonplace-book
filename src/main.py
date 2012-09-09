import webapp2
from test.testwebhandler import TestWebHandler
import os

routes = [
        ]

isdebug = os.environ.get('SERVER_SOFTWARE','').startswith('Development')

if isdebug:
    routes.append(('/tests', TestWebHandler))

app = webapp2.WSGIApplication(routes, debug=True)