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
    
    #metadata.drop_all(checkfirst=False)
    metadata.create_all()
    
    
    print "Adding data..."    
    tag1 = Tag(name='sci-fi')
    q1 = Quote(content="A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyze a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects.", who="Robert Heinlein")    
    tag1.quotes.append(q1)    
    tag2 = Tag(name='learning')
    q2 = Quote(content="Live as if you were to die tomorrow. Learn as if you were to live forever.", who="Mahatma Gandhi")    
    tag2.quotes.append(q2)
    tag3 = Tag(name='humour')
    q3 = Quote(content="In the beginning the Universe was created. This has made a lot of people very angry and has been widely regarded as a bad move.", who="Douglas Adams")
    tag3.quotes.append(q3)
    tag4 = Tag(name='science')
    q4 = Quote(content="I'll never make that mistake again, reading the experts' opinions. Of course, you only live one life, and you make all your mistakes, and learn what not to do, and that's the end of you.", who="Richard Feynman")
    tag4.quotes.append(q4)
    print "Adding users.... user 'admin' with role 'admin' ..."    
    print "Add group..."
    g = Group('everyone')    
    print "Add role..."
    role_admin = Role('admin')    
    print "Add user..."
    import sha
    hash = sha.new()
    hash.update('pylons')
    passwd = hash.digest()
    u = User(username='admin', password=passwd, email='admin@example.com')
    u.roles.append(role_admin)
    objectstore.flush()
    print "done populating data..."  
