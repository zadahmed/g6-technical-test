from django.test import TestCase

from pulse_survey.survey import models


class FeedbackModelTest(TestCase):
    def test_feedback_saved(self):
        email = "Test@Example.Com"
        feedback = models.Feedback(email=email, content="Some feedback")
        feedback.save()
        self.assertEqual(feedback.email, email.lower())
        self.assertEqual(feedback.content, "Some feedback")
