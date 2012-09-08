from google.appengine.ext import ndb
from page import Page

class Chapter(ndb.Model):
    strUserId = ndb.StringProperty()
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strName = ndb.StringProperty()
    keysPage = ndb.KeyProperty(kind=Page, repeated=True)
