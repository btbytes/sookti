from sookti.tests import *

class TestFeedsController(TestController):
    def test_index(self):
        response = self.app.get(url_for(controller='feeds'))
        # Test response...