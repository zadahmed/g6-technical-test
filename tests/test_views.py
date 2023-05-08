import uuid
from django.test import TestCase


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    
    def test_location_page(self):
        session_id = uuid.uuid4()
        response = self.client.get(f"/survey/{session_id}/location-question/")
        self.assertEqual(response.status_code, 200)