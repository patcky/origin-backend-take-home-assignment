from django.test import TestCase

from insurance_quote_api.serializers import *

class TestInsuranceQuoteSerializers(TestCase):
    @classmethod
    def setUp(self):
        # generate data sample that will be used in other methods
        pass

    def test_validate_empty_data(self):
        # try passing empty data and checking if the serializer returns an error with the missing fields
        pass

    def test_validate_incomplete_data(self):
        # try passing incomplete data and checking if the serializer returns an error with the missing fields
        pass

    def test_validate_complete_data(self):
        # try passing data with complete data and checking if the serializer validates the fields
        pass

    def test_validate_wrong_format_data(self):
        # try passing wrong format data and checking if the serializer returns an error
        pass
