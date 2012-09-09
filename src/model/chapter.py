from google.appengine.ext import ndb
from page import Page
from user import User
from model import ProcessStandardParams, Fetch
from service.messages import ConstructChaptersMessage

class Chapter(ndb.Model):
    keyUser = ndb.KeyProperty(kind = User)
    dtCreated = ndb.DateTimeProperty(auto_now_add = True)
    dtUpdated = ndb.DateTimeProperty(auto_now = True)
    
    strName = ndb.StringProperty()
    keysPage = ndb.KeyProperty(kind=Page, repeated=True)

    @classmethod
    def ProcessQueryMessage(cls, aChapterQueryMessage):
        lquery = ProcessStandardParams(aChapterQueryMessage, Page)
        
        lquery = lquery.order(-Chapter.dtCreated)

        lchapters, lcursor, lmore = Fetch(aChapterQueryMessage, lquery)
            
        retval = ConstructChaptersMessage(lchapters, lcursor, lmore)

        return retval
        
    @classmethod
    def ProcessUpdateMessage(cls, aChapterMessage):
        lchapterKey = ndb.Key(Page, aChapterMessage.key)
        lchapter = lchapterKey.get()
        
        if not lchapter:
            lchapter = Page(key = lchapterKey)
            lchapter.keyUser = User.GetCurrentUser()
        else:
            if not lchapter.keyUser == User.GetCurrentUser().key:
                raise Exception("Not authorised")

        lchapter.strName = aChapterMessage.name
        if aChapterMessage.pages:
            lchapterPages = []
            for lpageKey in aChapterMessage.pages:
                lchapterPages.append(ndb.Key(Page, lpageKey))
            lchapter.keysPage = lchapterPages

        lchapter.put()
    
    @classmethod
    def ProcessDelete(cls, aChapterKey):
        lchapter = aChapterKey.get()
        
        if lchapter:
            if not lchapter.keyUser == User.GetCurrentUser().key:
                raise Exception("Not authorised")

            aChapterKey.delete()
    
