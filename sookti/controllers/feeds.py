from sookti.lib.base import *

class FeedsController(BaseController):
    
    def index(self):        
        return Response('Welcome to Feeds')
        
    def random(self):
        return render_reponse('mako', '/feeds/index.mak')
        
