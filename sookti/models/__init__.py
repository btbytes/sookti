from elixir import *
from sqlalchemy import func
import time
from datetime import datetime

class Quote(Entity):
    with_fields(
    content = Field(Unicode(), nullable='False'),
    who = Field(Unicode(40)),
    lang = Field(String(10), default='English'),
    timestamp = Field(DateTime, default=func.now()))

    def __repr__(self):
        return '<Quote %s -- %s>' % (self.content[:20], self.who)

        
    
    