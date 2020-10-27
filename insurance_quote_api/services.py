from abc import ABC, abstractmethod
from insurance_quote_api.models import RiskProfilePlan, RiskProfileRecommendation
from insurance_quote_api.rules import *


class InsuranceRiskProfile(ABC):
    """Base service class for generating profiles according to business rules (available plans). 
    Other specific profile classes will inherit base methods from this."""

    def __init__(self):
        self.rules = []

    def calculate_score(self, user_data):
        """Returns total score for analyzed profile type"""

        score = user_data.base_score()
        for rule in self.rules:
            score += rule.calculate(user_data)

        return score

    def evaluate(self, user_data):
        """Checks if user is eligible to the plan and calls self.calculate_score()"""

        if self.check_eligibility(user_data) == False:
            return RiskProfileRecommendation.INELIGIBLE

        score = self.calculate_score(user_data)
        return self.get_user_profile(score)

    def check_eligibility(self, user_data):
        """This function should be defined in each specific profile"""
        pass

    def get_user_profile(self, score):
        """Returns instance of RiskProfileRecommendation based on score"""

        if score <= 0:
            return RiskProfileRecommendation.ECONOMIC
        elif score <= 2:
            return RiskProfileRecommendation.REGULAR
        else:
            return RiskProfileRecommendation.RESPONSIBLE

class LifeInsuranceRiskProfile(InsuranceRiskProfile):
    """Defines which rules are applied to Life Insurance profile and what is eligibility criteria.
    Inherits methods from InsuranceRiskProfile."""

    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            HighIncomeRuleStrategy(-1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(1),
        ]

    def check_eligibility(self, user_data):
        """Checks eligibility criteria"""

        return user_data.age <= 60


class DisabilityInsuranceRiskProfile(InsuranceRiskProfile):
    """Defines which rules are applied to Disability Insurance profile and what is eligibility criteria.
    Inherits methods from InsuranceRiskProfile."""
    
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            HighIncomeRuleStrategy(-1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(-1),
        ]

    def check_eligibility(self, user_data):
        """Checks eligibility criteria"""
        if user_data.house is not None:
            self.rules.append(HouseMortgagedRuleStrategy(1))
            
        has_income = user_data.income > 0
        is_under_60_years = user_data.age <= 60
        return has_income and is_under_60_years

class HomeInsuranceRiskProfile(InsuranceRiskProfile):
    """Defines which rules are applied to Home Insurance profile and what is eligibility criteria.
    Inherits methods from InsuranceRiskProfile."""

    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            HighIncomeRuleStrategy(-1),
            HouseMortgagedRuleStrategy(1),
        ]

    def check_eligibility(self, user_data):
        """Checks eligibility criteria"""
        return user_data.house is not None

class AutoInsuranceRiskProfile(InsuranceRiskProfile):
    """Defines which rules are applied to Auto Insurance profile and what is eligibility criteria.
    Inherits methods from InsuranceRiskProfile."""
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            VehicleHasLessThan5Years(1),
            HighIncomeRuleStrategy(-1),
        ]

    def check_eligibility(self, user_data):
        """Checks eligibility criteria"""
        return user_data.vehicle is not None

class InsuranceService:
    """Has a method analyze, that receives user data and returns a RiskProfilePlan object."""

    def analyze(self, user_data):
        """Builds a RiskProfilePlan with all insurance categories. 
        Needs to receive user_data as a @dataclass structure. Returns a RiskProfilePlan object."""

        return RiskProfilePlan(
            life=LifeInsuranceRiskProfile().evaluate(user_data),
            disability=DisabilityInsuranceRiskProfile().evaluate(user_data),
            home=HomeInsuranceRiskProfile().evaluate(user_data),
            auto=AutoInsuranceRiskProfile().evaluate(user_data),
        )

