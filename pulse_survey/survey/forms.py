
from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    if not email_address.endswith("@cabinetoffice.gov.uk"):
        raise ValidationError("Only Cabinet Office email addresses are allowed.")
    return True
    


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

