
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(value):
    # TODO - update this for CO emails
    pass


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

