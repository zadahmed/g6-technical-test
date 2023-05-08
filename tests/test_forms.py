from django.test import TestCase, SimpleTestCase

from pulse_survey.survey import forms


class FeedbackFormTest(TestCase):
    def test_incorrect_email(self):
        form = forms.FeedbackForm({"email": "not an email",
            "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Enter a valid email address" in str(email_errors))

    def test_correct_email(self):
        form = forms.FeedbackForm({"email": "test@example.com", "content": "some feedback"})
        form.is_valid()
        no_email_errors = "email" not in form.errors
        self.assertTrue(no_email_errors)
