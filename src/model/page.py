from google.appengine.ext import ndb

class Page(ndb.Model):
    strUserId = ndb.StringProperty()
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strUrl = ndb.StringProperty()
    strName = ndb.StringProperty()
    txtDescription = ndb.TextProperty()
    
    strImageUrl = ndb.StringProperty()
    strType = ndb.StringProperty()
