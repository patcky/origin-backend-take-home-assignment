from django.test import TestCase

from insurance_quote_api.rules import *

class TestInsuranceQuoteRules(TestCase):
    @classmethod
    def setUp(self):
        """Generates data sample that will be used in other methods"""
        self.user_data = UserData(
            age=35,
            dependents=2,
            house=HouseStatus(OwnershipStatus.OWNED),
            income=100,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[0, 1, 0],
            vehicle=VehicleData(year=2018),
        )
        self.base_score = 0
        self.rule_score = 1

    def test_less_than_30_years_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        self.user_data.age = 25
        self.base_score += LessThan30YearsRuleStrategy(self.rule_score).calculate(self.user_data)
        assert self.base_score == 1

    def test_less_than_30_years_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        self.base_score += LessThan30YearsRuleStrategy(self.rule_score).calculate(self.user_data)
        assert self.base_score == 0

    def test_between_30_and_40_years_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        self.base_score += Between30And40YearsRuleStrategy(self.rule_score).calculate(self.user_data)
        assert self.base_score == 1

    def test_between_30_and_40_years_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        self.user_data.age = 25
        self.base_score += Between30And40YearsRuleStrategy(self.rule_score).calculate(self.user_data)
        assert self.base_score == 0

        self.age = 45
        self.base_score += Between30And40YearsRuleStrategy(self.rule_score).calculate(self.user_data)
        assert self.base_score == 0

    def test_high_income_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_high_income_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_house_mortgaged_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_house_mortgaged_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_has_dependents_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_has_dependents_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_is_married_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_is_married_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_vehicle_has_less_than_5_years_rule_strategy_is_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass

    def test_vehicle_has_less_than_5_years_rule_strategy_is_not_applied(self):
        # test passing a score and user data to the rule and checking if it was applied
        pass