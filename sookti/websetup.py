import paste.deploy
from elixir import *
from sookti.models import *
import time
from sqlalchemy import create_session

def setup_config(command, filename, section, vars):
    """
    Place any commands to setup sookti here.
    """
    conf = paste.deploy.appconfig('config:' + filename)
    paste.deploy.CONFIG.push_process_config({'app_conf':conf.local_conf,
                                             'global_conf':conf.global_conf})
    
    metadata.connect(conf['sqlalchemy.dburi'])
    
    metadata.drop_all(checkfirst=False)
    metadata.create_all()
    
    
    print "Adding data..."    
    tag1 = Tag(name='default')
    q1 = Quote(content="First they laugh at you...", who="Gandhi")
    tag1.quotes.append(q1)    
    print "Adding users.... user 'admin' with role 'admin' ..."    
    print "Add group..."
    g = Group('everyone')    
    print "Add role..."
    role_admin = Role('admin')    
    print "Add user..."
    u = User(username='admin', password='pylons', email='admin@example.com')
    u.roles.append(role_admin)
    objectstore.flush()
    print "done populating data..."  