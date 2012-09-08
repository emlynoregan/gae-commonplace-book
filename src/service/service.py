from protorpc import messages
import time

class ChapterQueryMessage(messages.Message):
    key = messages.StringField(1)
    limit = messages.IntegerField(2, default = 10)
    cursor = messages.StringField(3)

class ChapterMessage(messages.Message):
    key = messages.StringField(1)
    
    user = messages.StringField(2)
    
    created = messages.IntegerField(4)
    updated = messages.IntegerField(5)

    name = messages.StringField(6)
    pages = messages.StringField(7, repeated=True)
    
def ConstructChapterMessage(aPage):
    luserMessage = ChapterMessage()
    luserMessage.key = unicode(aPage.key)
    luserMessage.user = unicode(aPage.keyUser)
    luserMessage.created = int(time.mktime(aPage.dtCreated.timetuple()))
    luserMessage.updated = int(time.mktime(aPage.dtUpdated.timetuple()))
    luserMessage.name = aPage.strName
    if aPage.keysPage:
        lpages = []
        for lkeyPage in aPage.keysPage:
            lpages.append(unicode(lkeyPage))
        luserMessage.pages = lpages
    return luserMessage

class ChaptersMessage(messages.Message):
    users = messages.MessageField(ChapterMessage, 1, repeated=True)
    cursor = messages.StringField(2)
    more = messages.BooleanField(3)
    
def ConstructChaptersMessage(aChapters, aCursor, aMore):
    luserMessages = []
    for luser in aChapters:
        luserMessage = ConstructChapterMessage(luser)
        luserMessages.append(luserMessage)

    retval = ChapterMessage()    
    retval.users = luserMessages
    retval.cursor = aCursor.urlsafe()
    retval.more = aMore
    return retval

class PageQueryMessage(messages.Message):
    key = messages.StringField(1)
    limit = messages.IntegerField(2, default = 10)
    cursor = messages.StringField(3)
    userkey = messages.StringField(4)

class PageMessage(messages.Message):
    key = messages.StringField(1)
    
    user = messages.StringField(2)
    
    created = messages.IntegerField(4)
    updated = messages.IntegerField(5)

    url = messages.StringField(6)
    name = messages.StringField(7)
    description = messages.StringField(8)
    imageurl = messages.StringField(9)
    type = messages.StringField(10)
    
def ConstructPageMessage(aPage):
    lpageMessage = PageMessage()
    lpageMessage.key = unicode(aPage.key)
    lpageMessage.user = unicode(aPage.keyUser)
    lpageMessage.created = int(time.mktime(aPage.dtCreated.timetuple()))
    lpageMessage.updated = int(time.mktime(aPage.dtUpdated.timetuple()))
    lpageMessage.url = aPage.strUrl
    lpageMessage.name = aPage.strName
    lpageMessage.description = aPage.strDescription
    lpageMessage.imageurl = aPage.strImageUrl
    lpageMessage.type = aPage.strType
    return lpageMessage

class PagesMessage(messages.Message):
    pages = messages.MessageField(PageMessage, 1, repeated=True)
    cursor = messages.StringField(2)
    more = messages.BooleanField(3)
    
def ConstructPagesMessage(aPages, aCursor, aMore):
    lpageMessages = []
    for lpage in aPages:
        lpageMessage = ConstructPageMessage(lpage)
        lpageMessages.append(lpageMessage)

    retval = PageMessage()    
    retval.pages = lpageMessages
    retval.cursor = aCursor.urlsafe()
    retval.more = aMore
    return retval

class UserQueryMessage(messages.Message):
    key = messages.StringField(1) # if not provided, it'll return the logged in user.

class UserMessage(messages.Message):
    key = messages.StringField(1)
    
    created = messages.IntegerField(4)
    updated = messages.IntegerField(5)

    userid = messages.StringField(6)
    email = messages.StringField(7)
    nickname = messages.StringField(8)
    
def ConstructUserMessage(aUser):
    luserMessage = UserMessage()
    luserMessage.key = unicode(aUser.key)
    luserMessage.created = int(time.mktime(aUser.dtCreated.timetuple()))
    luserMessage.updated = int(time.mktime(aUser.dtUpdated.timetuple()))
    luserMessage.userid = aUser.strUserId
    luserMessage.email = aUser.strEmail
    luserMessage.nickname = aUser.strNickname
    return luserMessage

class UsersMessage(messages.Message):
    users = messages.MessageField(UserMessage, 1, repeated=True)
    cursor = messages.StringField(2)
    more = messages.BooleanField(3)
    
def ConstructUsersMessage(aUsers, aCursor, aMore):
    luserMessages = []
    for luser in aUsers:
        luserMessage = ConstructUserMessage(luser)
        luserMessages.append(luserMessage)

    retval = UserMessage()    
    retval.users = luserMessages
    retval.cursor = aCursor.urlsafe()
    retval.more = aMore
    return retval

