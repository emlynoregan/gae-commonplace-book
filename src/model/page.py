from google.appengine.ext import ndb
from user import User

class Page(ndb.Model):
    keyUser = ndb.KeyProperty(kind = User)
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strUrl = ndb.StringProperty()
    strName = ndb.StringProperty()
    txtDescription = ndb.TextProperty()
    
    strImageUrl = ndb.StringProperty()
    strType = ndb.StringProperty()
