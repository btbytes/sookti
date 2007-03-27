from elixir import *
from sqlalchemy import func, DynamicMetaData
import time, datetime
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
        ts_updated = Field(TIMESTAMP(timezone=True), onupdate=func.now())
    )
    has_and_belongs_to_many('tags', of_kind='Tag', inverse='quotes')
    
    def __repr__(self):
        return '<Quote %s -- %s>' % (self.content[:20], self.who)

    def __str__(self):
        return '%s... -- %s' % (self.content[:20], self.who)
    
    def now():
        return datetime.now(self.ts_updated.tzinfo)
    
class Tag(Entity):
    using_options(tablename='sookti_tags')
    with_fields(
        name = Field(Unicode(40), unique=True, nullable=False)
    )
    has_and_belongs_to_many('quotes', of_kind='Quote', inverse='tags')

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
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
        username   = Field(String(50), unique=True, nullable=False),
        password   = Field(String(255)),
        email      = Field(String(255)),
        fullaname  = Field(Unicode(255)), 
        lastlogin  = Field(TIMESTAMP(timezone=True), onupdate=func.now()),
        created    = Field(TIMESTAMP(timezone=True), default=func.now())        
    )
    has_and_belongs_to_many('groups', of_kind='Group', inverse='users')
    has_and_belongs_to_many('roles', of_kind='Role', inverse='users')
    
    def __repr__(self):
        return '<Tag "%s">' % self.username


class RegistrationProfile(Entity):
    using_options(tablename='sookti_registration_profile')
    with_fields(
        activation_key = Field(String(40)),
        key_generated  = Field(TIMESTAMP(timezone=True), default=func.now())
    )
    belongs_to('user', of_kind='User')
    
    def __str__(self):
        return "User Profile for %s " % self.username
    
    def activation_key_expired(self):
        """
        Determines whether this Profile's activation key has expired,
        based on the value of the setting ``ACCOUNT_ACTIVATION_DAYS``.
        
        """
        pass
        expiration_date = datetime.timedelta(days=7)
        return self.key_generated + expiration_date <= datetime.datetime.now()
        
