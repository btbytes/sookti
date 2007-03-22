from elixir import *
from sqlalchemy import func
import time
from datetime import datetime
import forms

class Quote(Entity):
    with_fields(
    content = Field(Unicode(), nullable='False'),
    who = Field(Unicode(40)),
    lang = Field(String(10), default='English'),
    ts_created = Field(DateTime, default=func.now()),
    ts_updated = Field(DateTime, onupdate=func.now())
    )
    using_options(tablename='sookti_quotes')
    has_and_belongs_to_many('tags', of_kind='Tag', inverse='quotes')
    def __repr__(self):
        return '<Quote %s -- %s>' % (self.content[:20], self.who)

class Tag(Entity):
    with_fields(
        name = Field(Unicode(40))
    )    
    using_options(tablename='sookti_tags')
    has_and_belongs_to_many('quotes', of_kind='Quote', inverse='tags')
    
    def __repr__(self):
        return '<Tag "%s">' % self.name
    