from django.test import TestCase, Client
from django.urls import reverse
from insurance_quote_api import views
import json

class TestInsuranceQuoteViews(TestCase):
    @classmethod
    def setUp(self):
        """Generates data sample that will be used in other methods"""
        self.user_data = {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }
        self.client = Client()
        self.url = reverse('quote')

    def test_make_post_call_with_empty_data(self):
        # try making a post call with empty data and checking if the view returns errors
        response = self.client.post(self.url)
        assert response.status_code == 400

    def test_make_post_call_with_complete_data(self):
        # try making a post call with complete data and checking if the view returns complete result
        response = self.client.post(self.url, json.dumps(self.user_data), content_type='application/json')
        assert response.status_code == 200

    def test_make_post_call_with_incomplete_data(self):
        # try making a post call with incomplete data and checking if the view returns errors
        del self.user_data["age"]
        del self.user_data["dependents"]
        response = self.client.post(self.url, json.dumps(self.user_data), content_type='application/json')
        assert response.status_code == 400

    def test_make_get_call(self):
        # try making a get call and checking if the view returns HTTP method not allowed
        response = self.client.get(self.url)
        assert response.status_code == 405