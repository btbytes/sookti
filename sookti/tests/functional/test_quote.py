from sookti.tests import *

class TestQuoteController(TestController):
    def test_index(self):
        response = self.app.get(url_for(controller='quote'))
        # Test response...