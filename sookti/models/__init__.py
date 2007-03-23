from elixir import *
from sqlalchemy import func, DynamicMetaData
import time
from datetime import datetime
import forms

metadata = DynamicMetaData()

class Quote(Entity):
    using_options(tablename='sookti_quotes')
    with_fields(
        content = Field(Unicode(), nullable='False'),
        who = Field(Unicode(40)),
        lang = Field(String(10), default='English'),
        ts_created = Field(DateTime, default=func.now()),
        ts_updated = Field(DateTime, onupdate=func.now())
    )    
    has_and_belongs_to_many('tags', of_kind='Tag', inverse='quotes')
    def __repr__(self):
        return '<Quote %s -- %s>' % (self.content[:20], self.who)

class Tag(Entity):
    using_options(tablename='sookti_tags')
    with_fields(
        name = Field(Unicode(40))
    )    
    has_and_belongs_to_many('quotes', of_kind='Quote', inverse='tags')
    
    def __repr__(self):
        return '<Tag "%s">' % self.name
    
class Group(Entity):
    using_options(tablename='sookti_group')
    with_fields(
        name = Field(String(50),unique=True, nullable=False)
    )
    has_and_belongs_to_many('users', of_kind='User', inverse='groups')
    
    def __repr__(self):
        return '<Tag "%s">' % self.name
    
    def __init__(self, name):
        self.name = name

class Role(Entity):
    using_options(tablename='sookti_role')
    with_fields(
        name = Field(String(50),unique=True, nullable=False)
    )
    has_and_belongs_to_many('users', of_kind='User', inverse='roles')
    
    def __repr__(self):
        return '<Tag "%s">' % self.name
        
    def __init__(self, name):
        self.name = name
        
class User(Entity):
    using_options(tablename='sookti_user')
    with_fields(
        username  = Field(String(50), unique=True, nullable=False),
        password  = Field(String(255)),
        email     = Field(String(255)),
        fullanme  = Field(Unicode(255)), 
        lastlogin = Field(DateTime, onupdate=func.now()),
        created   = Field(DateTime, default=func.now())
    )
    has_and_belongs_to_many('groups', of_kind='Group', inverse='users')
    has_and_belongs_to_many('roles', of_kind='Role', inverse='users')
    
    def __repr__(self):
        return '<Tag "%s">' % self.username
    
