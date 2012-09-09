from protorpc import remote
from model.user import User
from service.messages import KeyQueryMessage, UserMessage, PageQueryMessage, \
    PageMessage, PagesMessage, ChapterQueryMessage, ChapterMessage, ChaptersMessage, \
    ConstructUserMessage
from model.page import Page
from model.chapter import Chapter
from protorpc import message_types
from google.appengine.ext import ndb

class Service(remote.Service):
    
    @remote.method(KeyQueryMessage, UserMessage)
    def get_user(self, request):
        return ndb.Key(User, request.key).get()
    
    @remote.method(message_types.VoidMessage, UserMessage)
    def get_currentuser(self, request):
        return ConstructUserMessage(User.GetCurrentUser())

    @remote.method(KeyQueryMessage, PageMessage)
    def get_page(self, request):
        return ndb.Key(User, request.key).get()
    
    @remote.method(PageQueryMessage, PagesMessage)
    def get_pages(self, request):
        return Page.ProcessQueryMessage(request)
    
    @remote.method(PageMessage, message_types.VoidMessage)
    def update_page(self, request):
        Page.ProcessUpdateMessage(request)
    
    @remote.method(KeyQueryMessage, ChapterMessage)
    def get_chapter(self, request):
        return ndb.Key(Chapter, request.key).get()
    
    @remote.method(ChapterQueryMessage, ChaptersMessage)
    def get_chapters(self, request):
        return Chapter.ProcessQueryMessage(request)
    
    @remote.method(ChapterMessage, message_types.VoidMessage)
    def update_chapter(self, request):
        return Chapter.ProcessUpdateMessage(request)
    
    @remote.method(KeyQueryMessage, message_types.VoidMessage)
    def delete_chapter(self, request):
        return Chapter.ProcessDelete(ndb.Key(Chapter, request.key))
    