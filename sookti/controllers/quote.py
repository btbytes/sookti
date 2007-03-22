from sookti.lib.base import *
import formencode
import formbuild
from sookti import models

class QuoteController(BaseController):
    def index(self):        
        return render_response('mako', '/index.mak')
        
    def new(self):
        print 'DIR OF MODEL :::::',dir(model)
        '''
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
                c.content = 'content'
                c.who = 'who?'
                return render_response('mako', '/new_success.mak')
            
        else:  
            c.form = model.forms.build.StandardForm()
            return render_response('mako', '/quote_form.mak')
        '''
        results, errors, response = formbuild.handle(
            schema=model.forms.schema.EmailFormSchema(),
            template='quote_form.myt',
            form=model.forms.build.StandardForm
        )
        if response:
            return response
        return Response('mako', '/new_successs.mak')            
        
    def random(self):
        return render_response('mako', '/new.mak')
        
    def tag(self):
        return render_response('mako', '/tag.mak')
    
    def leaf(self,id):
        return render_response('mako', '/leaf.mak')