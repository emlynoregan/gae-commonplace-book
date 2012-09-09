import unittest
from google.appengine.ext import ndb
from model.user import User
from service.services import Service
from protorpc.message_types import VoidMessage
from service.messages import UserMessage

class UserTests(unittest.TestCase):
    
    fredkey = '4f99b3cf-6b26-4153-9cc6-faec093dfe04'
    
    def setUp(self):
        lfred = User(key = ndb.Key(User, self.fredkey), strUserId = "fred", strEmail = "fred@example.com", strNickname = "Freddy" )
        lfred.put()
    
    def tearDown(self):
        ndb.Key(User, self.fredkey).delete()

    def SetFredAsCurrentUser(self):    
        lfred = ndb.Key(User, self.fredkey).get()
        lfred.SetCurrentUser()

    def test001GetCurrentUser(self):
        self.SetFredAsCurrentUser()
        
        lrequest = VoidMessage()

        # raises exception if it fails        
        lresult = Service().get_currentuser(lrequest)
                
        self.assertIsNotNone(lresult, "lresult is None")
        self.assertIsInstance(lresult, UserMessage, "lresult is wrong class, %s" % lresult.__class__.__name__)

        self.assertEqual(lresult.key, self.fredkey, "Wrong user returned: %s" % lresult.key)

