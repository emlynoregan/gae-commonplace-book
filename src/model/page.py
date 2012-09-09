from google.appengine.ext import ndb
from user import User
from service.messages import ConstructPagesMessage
from model import ProcessStandardParams, Fetch

class Page(ndb.Model):
    keyUser = ndb.KeyProperty(kind = User)
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strUrl = ndb.StringProperty()
    strName = ndb.StringProperty()
    txtDescription = ndb.TextProperty()
    
    strImageUrl = ndb.StringProperty()
    strType = ndb.StringProperty()

    @classmethod
    def ProcessQueryMessage(cls, aPageQueryMessage):
        lquery = ProcessStandardParams(aPageQueryMessage, Page)
        
        lquery = lquery.order(-Page.dtCreated)

        lpages, lcursor, lmore = Fetch(aPageQueryMessage, lquery)
            
        retval = ConstructPagesMessage(lpages, lcursor, lmore)

        return retval
    
    @classmethod
    def ProcessUpdateMessage(cls, aPageMessage):
        lpageKey = ndb.Key(Page, aPageMessage.key)
        lpage = lpageKey.get()
        
        if not lpage:
            lpage = Page(key = lpageKey)
            lpage.keyUser = User.GetCurrentUser()
        else:
            if not lpage.keyUser == User.GetCurrentUser().key:
                raise Exception("Not authorised")

        lpage.strUrl = aPageMessage.url
        lpage.strName = aPageMessage.name
        lpage.strDescription = aPageMessage.description
        lpage.strImageUrl = aPageMessage.imageurl
        lpage.strType = aPageMessage.type

        lpage.put()
    