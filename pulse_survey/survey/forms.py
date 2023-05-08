
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    # TODO - update to raise a ValidationError for non-Cabinet Office emails
    return True
    


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

