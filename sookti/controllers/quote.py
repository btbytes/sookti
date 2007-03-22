from sookti.lib.base import *
import formencode
import formbuild
from sookti import models

class QuoteController(BaseController):
    def index(self):        
        return render_response('mako', '/index.mak')
        
    def new(self):        
        if len(request.params):
            try:
                results = model.forms.schema.QuoteFormSchema.to_python(
                    dict(request.params),
                    state=c
                )
            except formencode.Invalid, e:
                c.form = model.forms.build.StandardForm(
                    dict(request.params),
                    e.error_dict or {}
                )
                return render_response('mako', '/quote_form.mak')
            
            else:
                c.content = request.params['content']
                c.who = request.params['who']
                quote = model.Quote()
                quote.content = c.content
                quote.who = quote.who
                quote.flush()
                return render_response('mako', '/new_success.mak')
            
        else:  
            c.form = model.forms.build.StandardForm()
            return render_response('mako', '/quote_form.mak')
        
        
    def random(self):
        return render_response('mako', '/new.mak')
        
    def tag(self):
        return render_response('mako', '/tag.mak')
    
    def leaf(self,id):
        return render_response('mako', '/leaf.mak')