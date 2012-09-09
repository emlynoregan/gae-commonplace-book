from google.appengine.ext import ndb
from google.appengine.api import users

# tests can set a current user here
currentuser = None

class User(ndb.Model):
    strUserId = ndb.StringProperty()
    strEmail = ndb.StringProperty()
    strNickname = ndb.StringProperty()

    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)

    @classmethod
    def GetCurrentUser(cls):
        global currentuser
        
        if currentuser:
            retval = currentuser
        else:        
            retval = None
            lgoogleUser = users.get_current_user()
        
            if lgoogleUser:
                retval = User.query(User.strUserId == lgoogleUser.user_id()).get()
    
        return retval

    def SetCurrentUser(self):
        global currentuser
        currentuser = self
    