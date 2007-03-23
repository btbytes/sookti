from sookti.models import *
from sqlalchemy import *               
from logging import basicConfig, DEBUG, INFO, debug, info, warning, error, critical

basicConfig(level=DEBUG, format="%(levelname)s:%(module)s: %(message)s") # default WARNING
session = session_context.current
session.clear()            # remove stale info

def _downlist(thing):
    """Turn a string or tuple into a list and downcase it.
    """
    if isinstance(thing, tuple):
        thing = list(thing)
    elif isinstance(thing, str):
        thing = [thing]
    if not isinstance(thing, list):
        raise PermissionSetupError("Argument must be list, tuple or string, not: %s" % thing)
    return [t.lower() for t in thing]
def _getuser(environ):
    """Get the user from the environ, puke if none.
    """
    username = environ.get('REMOTE_USER')
    if not username:
        raise NotAuthenticatedError('Not Authenticated')
    user = session.query(User).get_by(username=username)
    debug("getuser user=%s" % user)
    if not user:
        warning("No user found with username=%s" % username)
        raise NotAuthorizedError("No user found with username=%s" % username)
    return user
    
class RoleIn(Permission):
    """Does the user have a role in the supplied list of roles (logical OR).
    A user can have more than one role.
    """
    def __init__(self, roles):
        self.roles = _downlist(roles)
    def check(self, app, environ, start_response):
        user = _getuser(environ)
        for role in user.roles:
            if role.name in self.roles:
                return app(environ, start_response)
        warning("User roles=%s not in required=%s" % (user.roles, self.roles))
        raise NotAuthorizedError("User roles=%s not in required=%s" % (user.roles, self.roles))
        
class GroupIn(Permission):
    """Is the users's group in the supplied list of groups (logical OR).
    A user can have only one group.
    """
    def __init__(self, groups):
        self.groups = _downlist(groups)
    def check(self, app, environ, start_response):
        user = _getuser(environ)
        if user.group.name in self.groups:
            return app(environ, start_response)
        warning("User group=%s not in required=%s" % (user.group, self.groups))
        raise NotAuthorizedError("User group=%s not in required=%s" % (user.group, self.groups))