from abc import ABC, abstractmethod
from insurance_quote_api.models import RiskProfilePlan, RiskProfileRecommendation
from insurance_quote_api.rules import *


class InsuranceRiskProfile(ABC):
    """Base service class for generating profiles according to business rules (available plans). 
    Other specific profile classes will inherit base methods from this."""

    def __init__(self):
        self.rules = []

    def calculate_score(self, analysis_data):
        """Returns total score for analyzed profile type"""

        score = analysis_data.base_score()
        for rule in self.rules:
            score += rule.calculate(analysis_data)

        return score

    def evaluate(self, analysis_data):
        """Checks if user is eligible to the plan and calls self.calculate_score()"""

        if self.check_eligibility(analysis_data) == False:
            return RiskProfileRecommendation.INELIGIBLE

        score = self.calculate_score(analysis_data)
        return self.get_user_profile(score)

    def check_eligibility(self, analysis_data):
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

    def check_eligibility(self, analysis_data):
        """Checks eligibility criteria"""
        return analysis_data.age <= 60


class DisabilityInsuranceRiskProfile(InsuranceRiskProfile):
    """Defines which rules are applied to Disability Insurance profile and what is eligibility criteria.
    Inherits methods from InsuranceRiskProfile."""
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            HighIncomeRuleStrategy(-1),
            HouseMortgagedRuleStrategy(1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(-1),
        ]

    def check_eligibility(self, analysis_data):
        """Checks eligibility criteria"""
        has_income = analysis_data.income > 0
        is_under_60_years = analysis_data.age <= 60
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

    def check_eligibility(self, analysis_data):
        """Checks eligibility criteria"""
        return analysis_data.house is not None

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

    def check_eligibility(self, analysis_data):
        """Checks eligibility criteria"""
        return analysis_data.vehicle is not None

class InsuranceService:
    """Builds a RiskProfilePlan with all insurance categories, calling 'evaluate' on each one. 
    Needs to receive analysis_data as a @dataclass structure."""
    def analysis(self, analysis_data):
        return RiskProfilePlan(
            life=LifeInsuranceRiskProfile().evaluate(analysis_data),
            disability=DisabilityInsuranceRiskProfile().evaluate(analysis_data),
            home=HomeInsuranceRiskProfile().evaluate(analysis_data),
            auto=AutoInsuranceRiskProfile().evaluate(analysis_data),
        )

