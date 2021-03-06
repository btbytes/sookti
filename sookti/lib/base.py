from pylons import Response, c, g, cache, request, session
from pylons.controllers import WSGIController
from pylons.decorators import jsonify, validate
from pylons.templating import render, render_response
from pylons.helpers import abort, redirect_to, etag_cache
from pylons.i18n import N_, _, ungettext
import sookti.models as model
import sookti.lib.helpers as h
from elixir import objectstore

class BaseController(WSGIController):
    def __call__(self, environ, start_response):
        # Insert any code to be run per request here. The Routes match
        # is under environ['pylons.routes_dict'] should you want to check
        # the action or route vars here
        model.metadata.connect(request.environ['paste.config']['app_conf']['sqlalchemy.dburi'])
        objectstore.clear()
        if session.has_key('flash'):
            c.flash = session['flash']
            del session['flash']
            session.save()            
        return WSGIController.__call__(self, environ, start_response)
        
    def flash(self, message):
        session['flash'] = message
        session.save()
# Include the '_' function in the public names
__all__ = [__name for __name in locals().keys() if not __name.startswith('_') \
           or __name == '_']
           
    