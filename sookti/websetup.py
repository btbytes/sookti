import paste.deploy
from elixir import *
from sookti.models import *


def setup_config(command, filename, section, vars):
    """
    Place any commands to setup sookti here.
    """
    conf = paste.deploy.appconfig('config:' + filename)
    paste.deploy.CONFIG.push_process_config({'app_conf':conf.local_conf,
                                             'global_conf':conf.global_conf})
    
    metadata.connect(conf['dsn'])
    metadata.create_all()
    import time
    tag1 = Tag(name='default')
    q1 = Quote(content="First they laugh at you...", who="Gandhi")
    tag1.quotes.append(q1) 
    objectstore.flush()
    
    print "done populating data..."
