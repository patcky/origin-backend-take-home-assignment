from django.test import TestCase

from insurance_quote_api.views import *

class TestInsuranceQuoteViews(TestCase):
    # These are e2e tests
    @classmethod
    def setUp(self):
        # generate data sample that will be used in other methods
        pass

    def test_make_post_call_with_empty_data(self):
        # try making a post call with empty data and checking if the view returns errors
        pass

    def test_make_post_call_with_complete_data(self):
        # try making a post call with complete data and checking if the view returns complete result
        pass

    def test_make_post_call_with_incomplete_data(self):
        # try making a post call with incomplete data and checking if the view returns errors
        pass

    def test_make_get_call(self):
        # try making a get call and checking if the view returns HTTP method not allowed
        pass