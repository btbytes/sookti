from sookti.lib.base import *
from sookti.lib.database import session_context
from sqlalchemy import *
from sookti.models import *
import datetime
from logging import basicConfig, DEBUG, INFO, debug, info, warning, error, critical
basicConfig(level=DEBUG, format="%(levelname)s:%(module)s: %(message)s") # default WARNING
from sookti.lib.base import *
from authkit.pylons_adaptors import authorize
from authkit.permissions import RemoteUser

class AccountController(BaseController):
    def __before__(self):
        self.session = session_context.current
        self.session.clear()            # remove stale info
        
    def index(self):
        return Response('')
        
    def signin(self):
        return render_response('mako',"/account_signin.mak")
        
    def signout(self):
        c.message = "You have been signed out."
        if request.environ.has_key('REMOTE_USER'):
            del request.environ['REMOTE_USER']
        return render_response('mako',"/account_signout.mak")
        
    # Want to use "signin" and distinguish by POST
    # I put a valid() in app_globals, but not using it now...
    # should move the lastlogin thing there if we gut this?
    def signin_check(self):
        debug("signin_check")
        username = request.params.get('username', '').strip().lower()
        password = request.params.get('password', '').strip()
        debug("signin_check username=%s password=%s" % (username, password))
        users = self.session.query(User).select_by(username=username)
        debug("signin_check users=%s" % users)
        # If I set c.message then return render_response(signin.myt)
        # will the next time through here see the referrer as this function?
        # If so we won't be able to redirect to where they came from,
        # and might have to save that state somewhere.
        if len(users) > 1:
            c.message="More than one user in database with username=%s found" % username
            return render_response('mako',"/account_signin.mak")
        elif not users:
            c.message="No such user %s" % username
            return render_response('mako',"/account_signin.mak")
        user = users[0]
        debug("user=%s" % user)
        debug("user.group=%s .roles=%s" % (user.groups, user.roles))
        # should this username/password check be done in middleware def valid(environ,username,password)?
        # see auth_tkt.py
        # see doing this in app_globals.py: http://authkit.org/docs/pylons.html
        if password != user.password:
            c.message="Bad password=%s for username=%s" % (password, username)
            return render_response('mako',"/account_signin.mak")
            #raise Exception("Bad password=%s for username=%s" % (password, username))
        request.environ['paste.auth_tkt.set_user'](username)
        user.lastlogin = datetime.datetime.now()
        self.session.save(user)
        self.session.flush()
        # on success return to referring page
        #redirect_to(request.environ['HTTP_REFERER'])
        redirect_to(controller='quote', action='index')