from google.appengine.ext import ndb
from page import Page
from user import User

class Chapter(ndb.Model):
    keyUser = ndb.KeyProperty(kind = User)
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strName = ndb.StringProperty()
    keysPage = ndb.KeyProperty(kind=Page, repeated=True)
