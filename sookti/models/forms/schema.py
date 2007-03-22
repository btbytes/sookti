import formencode

class QuoteFormSchema(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(not_empty=True)
    who = formencode.validators.String(not_empty=True)    
    tags = formencode.validators.String()
