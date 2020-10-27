from django.test import TestCase, Client

from insurance_quote_api.views import *

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

    def test_make_post_call_with_empty_data(self):
        # try making a post call with empty data and checking if the view returns errors
        self.user_data = {}

    def test_make_post_call_with_complete_data(self):
        # try making a post call with complete data and checking if the view returns complete result
        pass

    def test_make_post_call_with_incomplete_data(self):
        # try making a post call with incomplete data and checking if the view returns errors
        del self.user_data["age"]
        del self.user_data["dependents"]

    def test_make_get_call(self):
        # try making a get call and checking if the view returns HTTP method not allowed
        pass