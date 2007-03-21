import formencode

class QuoteFormSchema(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    quote = formencode.validators.String(not_empty=True)
    person = formencode.validators.String(not_empty=True)
