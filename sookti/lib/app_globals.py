class Globals(object):

    def __init__(self, global_conf, app_conf, **extra):
        """
        Globals acts as a container for objects available throughout
        the life of the application.

        One instance of Globals is created by Pylons during
        application initialization and is available during requests
        via the 'g' variable.
        
        ``global_conf``
            The same variable used throughout ``config/middleware.py``
            namely, the variables from the ``[DEFAULT]`` section of the
            configuration file.
            
        ``app_conf``
            The same ``kw`` dictionary used throughout
            ``config/middleware.py`` namely, the variables from the
            section in the config file for your application.
            
        ``extra``
            The configuration returned from ``load_config`` in 
            ``config/middleware.py`` which may be of use in the setup of
            your global variables.
            
        """
        from sookti.lib.database import session_context
        self.session = session_context.current
        self.session.clear()       
        
    def __del__(self):
        """
        Put any cleanup code to be run when the application finally exits 
        here.
        """
        pass

    def valid(self,environ, username, password):
        users = self.session.query(User).select_by(username=username)
        print "app_globals.valid users=%s" % users
        if len(users) > 1:
            print "app_globals.valid More than one user in database with username=%s found" % username
            return False
        elif not users:
            print "app_globals.valid No such user %s" % username
            return False
        if password == users[0].password:
            return True
        return False