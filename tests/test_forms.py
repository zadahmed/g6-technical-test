from django.test import TestCase, SimpleTestCase

from pulse_survey.survey import forms


class FeedbackFormTest(TestCase):
    def test_incorrect_email(self):
        invalid_cabinet_email = "invalid@hmrc.com"
        form = forms.FeedbackForm({"email": invalid_cabinet_email, "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue(
            "Only Cabinet Office email addresses are allowed." in str(email_errors)
        )

    def test_correct_email(self):
        valid_cabinet_email = "valid@cabinetoffice.gov.uk"
        form = forms.FeedbackForm(
            {"email": valid_cabinet_email, "content": "some feedback"}
        )
        form.is_valid()
        no_email_errors = "email" not in form.errors
        self.assertTrue(no_email_errors)


class CabinetOfficeValidationTest(SimpleTestCase):
    def test_is_cabinet_office_email(self):
        valid_email = "valid@cabinetoffice.gov.uk"
        result = forms.is_cabinet_office_email(valid_email)
        self.assertTrue(result)
