from abc import ABC, abstractmethod
from insurance_quote_api.models import *

class ScoreRuleStrategy(ABC):
    """Base class for the rules"""

    def calculate(self, user_data):
        pass

class LessThan30YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.age < 30:
            return self.__score

        return 0


class Between30And40YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.age >= 30 and user_data.age <= 40:
            return self.__score

        return 0


class HighIncomeRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.income > 200000:
            return self.__score

        return 0


class HouseMortgagedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.house.ownership_status == OwnershipStatus.MORTGAGED:
            return self.__score

        return 0


class HasDependentsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.dependents > 0:
            return self.__score

        return 0


class IsMarriedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.marital_status == MaritalStatus.MARRIED:
            return self.__score

        return 0


class VehicleHasLessThan5Years(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, user_data):
        if user_data.vehicle.years_old() <= 5:
            return self.__score

        return 0
