from rest_framework import serializers
from insurance_quote_api import models

class QuoteSerializer(serializers.Serializer):
    """Serializes (validates) the fields for the QuoteApiView's input"""

    age = serializers.IntegerField(min_value=0)
    dependents = serializers.IntegerField(min_value=0)
    income = serializers.IntegerField(min_value=0)

    MARITAL_STATUS_CHOICES = [
        "single",
        "married",
    ]
    marital_status = serializers.ChoiceField(MARITAL_STATUS_CHOICES)

    risk_questions = serializers.ListField(
        child=serializers.IntegerField(
            min_value=0, 
            max_value=1
        ),
        min_length=3, 
        max_length=3
    )

    vehicle = serializers.DictField(
        child=serializers.IntegerField(min_value=0),
        required=False, 
    )

    HOUSE_OWNERSHIP_CHOICES = [
        "owned",
        "mortgaged",
    ]

    house = serializers.DictField(
        child=serializers.ChoiceField(HOUSE_OWNERSHIP_CHOICES),
        required=False, 
    )