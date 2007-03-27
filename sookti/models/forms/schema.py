import formencode
import formencode.validators as forms

class QuoteFormSchema(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = forms.String(not_empty=True)
    who = forms.String(not_empty=True)    
    tags = forms.String()


class RegisterFormSchema(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = forms.String(not_empty=True)
    email = forms.Email()
    password1 = forms.String(not_empty=True)
    password2 = forms.String(not_empty=True)
    tos = forms.Bool()
    