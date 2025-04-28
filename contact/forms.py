from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)
#     # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             if field.widget.__class__.__name__ != 'ReCaptchaV2Checkbox':
#                 field.widget.attrs.update({'class': 'form-control'})

from  .models import Contact
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})