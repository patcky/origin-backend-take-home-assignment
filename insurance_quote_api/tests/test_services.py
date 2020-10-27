from django.test import TestCase

from insurance_quote_api.services import InsuranceService
from insurance_quote_api.models import *

class TestInsuranceQuoteService(TestCase):
    @classmethod
    def setUp(self):
        # I did the tests in normal pytest format, now I am trying to adapt into django, still wip
        return UserData(
            age=35,
            dependents=2,
            house=HouseStatus(OwnershipStatus.OWNED),
            income=100,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[0, 1, 0],
            vehicle=VehicleData(year=2018),
        )


    def test_complete_risk_profile_plan(self, user_data):
        profile = InsuranceService().analyze(user_data)    
        assert profile.auto == RiskProfileRecommendation.ECONOMIC
        assert profile.disability == RiskProfileRecommendation.ECONOMIC
        assert profile.home == RiskProfileRecommendation.ECONOMIC
        assert profile.life == RiskProfileRecommendation.REGULAR

    def test_risk_profile_with_zero_on_all_fields(self, user_data):
        user_data.age = 0
        user_data.dependents = 0
        user_data.house = 0
        user_data.income = 0
        user_data.risk_questions=[0, 0, 0]
        user_data.vehicle = 0
        profile = InsuranceService().analyze(user_data)

        assert profile.auto == RiskProfileRecommendation.INELIGIBLE
        assert profile.disability == RiskProfileRecommendation.INELIGIBLE
        assert profile.home == RiskProfileRecommendation.INELIGIBLE
        assert profile.life == RiskProfileRecommendation.ECONOMIC


    def test_user_without_car_is_ineligible_for_auto(self, user_data):
        user_data.vehicle = None
        profile = InsuranceService().analyze(user_data)

        assert profile.auto == RiskProfileRecommendation.INELIGIBLE


    def test_user_without_house_is_ineligible_for_home(self, user_data):
        user_data.house = None
        profile = InsuranceService().analyze(user_data)

        assert profile.home == RiskProfileRecommendation.INELIGIBLE


    def test_user_without_income_is_ineligible_for_disability(self, user_data):
        user_data.income = 0
        profile = InsuranceService().analyze(user_data)

        assert profile.disability == RiskProfileRecommendation.INELIGIBLE

    def test_user_under_30_years_is_economic(self, user_data):
        user_data.age = 20
        profile = InsuranceService().analyze(user_data)
        
        assert profile.auto == RiskProfileRecommendation.ECONOMIC
        assert profile.disability == RiskProfileRecommendation.ECONOMIC
        assert profile.home == RiskProfileRecommendation.ECONOMIC
        assert profile.life == RiskProfileRecommendation.ECONOMIC


    def test_user_over_60_year_is_ineligible_for_disability_and_life(self, user_data):
        user_data.age = 90
        profile = InsuranceService().analyze(user_data)

        assert profile.disability == RiskProfileRecommendation.INELIGIBLE
        assert profile.life == RiskProfileRecommendation.INELIGIBLE

    def test_user_with_high_income(self, user_data):
        user_data.income = 300000
        profile = InsuranceService().analyze(user_data)

        assert profile.auto == RiskProfileRecommendation.ECONOMIC

    def test_user_house_is_mortgaged(self, user_data):
        user_data.house = HouseStatus(OwnershipStatus.MORTGAGED)
        profile = InsuranceService().analyze(user_data)

        assert profile.home == RiskProfileRecommendation.ECONOMIC

    def test_user_single_without_dependents(self, user_data):
        user_data.dependents = 0
        profile = InsuranceService().analyze(user_data)

        assert profile.life == RiskProfileRecommendation.ECONOMIC
