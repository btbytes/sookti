from sookti.lib.base import *
import formencode
import formbuild
from sookti import models
from sookti.lib.base import *
from sookti.lib.database import session_context
from sqlalchemy import *
from sookti.models import *
import datetime
from logging import basicConfig, DEBUG, INFO, debug, info, warning, error, critical
basicConfig(level=DEBUG, format="%(levelname)s:%(module)s: %(message)s") # default WARNING
from sookti.lib.base import *
from authkit.pylons_adaptors import authorize
from authkit.permissions import RemoteUser

class QuoteController(BaseController):
    def __before__(self):
        self.session = session_context.current
        self.session.clear()            # remove stale info

    def index(self):
        c.quote = self.session.query(Quote).order_by([desc(Quote.c.ts_created)])[0]    
        return render_response('mako', '/index.mak')
        
        
    def view(self,id):
        c.quote = self.session.query(Quote).select_by(Quote.c.id==id)[0]    
        return render_response('mako', '/index.mak')
    
    @authorize(RemoteUser())            
    def edit(self,id):
        if len(request.params):
            try:
                results = model.forms.schema.QuoteFormSchema.to_python(
                    dict(request.params),
                    state=c
                )
                debug("result of for post=%s" % results)
            except formencode.Invalid, e:
                c.form = model.forms.build.StandardForm(
                    dict(request.params),
                   e.error_dict or {}
                )
                return render_response('mako', '/quote_form.mak')            
            else:
                quote = model.Quote.get_by(id=id)
                if not quote:
                    quote = model.Quote()
                c.content = request.params['content']
                c.who = request.params['who']
                c.tags = request.params['tags']
                quote.content = c.content
                quote.who = c.who
                for tag in c.tags.split(','):
                    if len(tag)>1:
                        try:                            
                            t = model.Tag(tag.strip())
                            t.flush()
                            print '$'*40, t, quote.tags
                            if t not in quote.tags:
                                quote.tags.append(t)
                                quote.flush()                                
                        except:
                            pass
                quote.flush()
                redirect_to(action="index")
                
        else:
            quote = model.Quote.get_by(id=id)
            if quote:
                data = {'content': quote.content,
                    'who':quote.who,
                    'ts_created': quote.ts_created,
                    'ts_updated': quote.ts_updated,
                    'tags': ','.join([str(tag) for tag in quote.tags]),
                    }
                c.form = model.forms.build.StandardForm(
                        dict(data)
                    )
            else:
                c.form = model.forms.build.StandardForm(                    
                    )
            return render_response('mako', '/quote_form.mak')       
        
    @authorize(RemoteUser())
    def delete(self,id):
        quote = model.Quote.get_by(id=id)          
        quote.delete()
        quote.flush()
        c.quotes = self.session.query(Quote).order_by([desc(Quote.c.ts_created)])          
        redirect_to(action="list")
        
    def random(self):
        c.quote = self.session.query(Quote).order_by(func.random())[0]
        return render_response('mako', '/index.mak')
        
    def tag(self,id):
        c.tag = id
        print '*'*30, dir(model.Quote)
        tag = self.session.query(Tag).get_by(Tag.c.name==id)
        c.quotes = tag.quotes
        c.message = 'Quotes tagged with %s' % tag
        return render_response('mako', '/quotes_list.mak')
    
    def leaf(self,id):
        return render_response('mako', '/leaf.mak')
    
    def list(self,id):
        c.quotes = self.session.query(Quote).order_by([desc(Quote.c.ts_created)])
        return render_response('mako', '/quotes_list.mak')
        
