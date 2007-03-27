import datetime, sha
from sqlalchemy import *
from sookti.models import *
from sookti.lib.base import *
from sookti.lib.database import session_context
from logging import basicConfig, DEBUG, INFO, debug, info, warning, error, critical
basicConfig(level=DEBUG, format="%(levelname)s:%(module)s: %(message)s") # default WARNING
from authkit.pylons_adaptors import authorize
from authkit.permissions import RemoteUser
from pylons.decorators import rest

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
        username = request.params.get('username', '').strip().lower()
        password = request.params.get('password', '').strip()        
        users = self.session.query(User).select_by(username=username)        
        hash = sha.new()
        hash.update(password)        
        password_digest = hash.digest()
        
        if len(users) > 1:
            c.message="More than one user in database with username=%s found" % username
            return render_response('mako',"/account_signin.mak")
        elif not users:
            c.message="No such user %s" % username
            return render_response('mako',"/account_signin.mak")
        user = users[0]
        print '-'*80, 'password', password_digest, 'user.password', user.password        
        
        if password_digest != user.password:
            c.message="Bad password=%s for username=%s" % (password, username)
            return render_response('mako',"/account_signin.mak")
            
        request.environ['paste.auth_tkt.set_user'](username)
        user.lastlogin = datetime.now()
        self.session.save(user)
        self.session.flush()        
        redirect_to(controller='quote', action='index')        
    
    @rest.dispatch_on(POST='register_user')
    def register(self):
        c.form = model.forms.build.StandardForm(
                        dict(request.params)
                    )
        return render_response('mako', '/registration/registration_form.mak')
    
    def register_user(self):
        return render_response('mako', '/leaf.mak')
    
    def activate(self,activation_key):
        return Response("Activate")
    
    def register_complete(self):
        return Response("Registration Successful")
        
        
    