import webapp2
import unittest
from usertests import UserTests

class TestWebHandler(webapp2.RequestHandler):

    def post(self):

        ltestClasses = [
            UserTests
        ]

        success = True
        suite = load_tests(unittest.TestLoader(), ltestClasses)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        success = success and result.wasSuccessful()

        if not success:
            self.response.status = 400
            
def load_tests(loader, test_classes):
    suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
    