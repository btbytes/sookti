engine = None
import sqlalchemy
from sqlalchemy.ext.sessioncontext import SessionContext
from sookti.models import metadatadata
from paste.deploy.converters import asbool

def get_engine():
    "Retreives the engine based on the current configuration"
    global engine
    if not engine:
        from paste.deploy import CONFIG
        config = CONFIG['app_conf']
        dburi = config.get("sqlalchemy.dburi")
        if not dburi:
            raise KeyError("No sqlalchemy database config found!")
        echo = asbool(config.get("sqlalchemy.echo", False))
        engine = sqlalchemy.create_engine(dburi, echo=echo)
        metadata.connect(engine)
    elif not metadata.is_bound():
        metadata.connect(engine)
    return engine
    
# a function to return a session bound to our engine
def make_session():
    return sqlalchemy.create_session(bind_to=get_engine())
    
# create SessionContext with our make_session function
session_context = SessionContext(make_session)