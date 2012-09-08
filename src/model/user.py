from google.appengine.ext import ndb

class User(ndb.Model):
    strUserId = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strNickname = ndb.StringProperty()

    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
