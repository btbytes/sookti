from sookti.lib.base import *
import formencode
import formbuild
from sookti import models
from sookti.lib.base import *
from sookti.lib.database import session_context
from sqlalchemy import *
from sookti.models import *
import datetime, random
from logging import basicConfig, DEBUG, INFO, debug, info, warning, error, critical
basicConfig(level=DEBUG, format="%(levelname)s:%(module)s: %(message)s") # default WARNING
from sookti.lib.base import *
from authkit.pylons_adaptors import authorize
from authkit.permissions import RemoteUser
from webhelpers.pagination import paginate, Paginator

items_per_page = 2
def page_offset(page,items_per_page=items_per_page):
    return (page - 1) * items_per_page
    
class QuoteController(BaseController):
    def __before__(self):
        self.session = session_context.current
        self.session.clear()

    def index(self):
        c.quote = self.session.query(Quote).order_by([desc(Quote.c.ts_created)])[0]    
        return render_response('mako', '/index.mak')
        
        
    def view(self,id):
        if not id: id = 1
        c.quote = self.session.query(Quote, limit=1).select_by(Quote.c.id==id)[0]
        return render_response('mako', '/index.mak')
    
    def random(self):
        item_count = self.session.query(Quote).count()
        id = random.randint(1,item_count)
        redirect_to(action="view", id=id)        
        
    def tag(self,id,page=1):
        c.tag = id
        page = int(page)
        offset= page_offset(page)
        item_count = self.session.query(Quote).count()
        c.paginator = Paginator(item_count, items_per_page, page)        
        tag = self.session.query(Tag).get_by(Tag.c.name==id)
        c.quotes = tag.quotes
        c.message = 'Quotes tagged with %s' % tag
        return render_response('mako', '/paginated_tag.mak')
    
    def tags(self,id):
        c.tags = self.session.query(Tag).select()        
        return render_response('mako', '/tags.mak')
    
    def page(self,id):                       
        if not id:
            page = 1
        else: page = int(id)                
        offset= page_offset(page)
        item_count = self.session.query(Quote).count()
        print '^'*80, "No of quotes:", item_count
        c.paginator = Paginator(item_count, items_per_page, page)        
        c.quotes = self.session.query(Quote, offset=offset, limit=items_per_page).order_by([desc(Quote.c.ts_created)])        
        return render_response('mako', '/paginated_list.mak')
    
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
                quote.content = results['content']
                quote.who = results['who']
                for tag in results['tags'].split(','):
                    tag = tag.strip(' ')                                            
                    t = model.Tag.get_by(name=tag)                                
                    if not t:
                        t = model.Tag(tag.strip())
                        t.flush()                                               
                    if t not in quote.tags:
                        quote.tags.append(t)
                quote.flush()
                self.flash("Created new...")                
                redirect_to(action="view", id=quote.id)
                
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
                self.flash("Creating a new Quote")
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
        
    
    @authorize(RemoteUser())
    def user(self,id):
        user = self.session.query(User, limit=1).select_by(username=id)[0]
        return Response('User %s' % user.username)
        