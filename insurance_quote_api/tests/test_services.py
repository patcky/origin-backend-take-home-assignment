from django.test import TestCase

from insurance_quote_api.services import InsuranceService
from insurance_quote_api.models import *

class TestInsuranceQuoteService(TestCase):
    @classmethod
    def setUp(self):
        return AnalysisData(
            age=35,
            dependents=2,
            house=HouseStatus(OwnershipStatus.OWNED),
            income=100,
            marital_status=MaritalStatus.MARRIED,
            risk_questions=[0, 1, 0],
            vehicle=VehicleData(year=2018),
        )


    def test_complete_risk_profile_plan(self, analysis_data):
        profile = InsuranceService().analysis(analysis_data)    
        assert profile.auto == RiskProfileRecommendation.ECONOMIC
        assert profile.disability == RiskProfileRecommendation.ECONOMIC
        assert profile.home == RiskProfileRecommendation.ECONOMIC
        assert profile.life == RiskProfileRecommendation.REGULAR

    def test_risk_profile_with_zero_on_all_fields(self, analysis_data):
        analysis_data.age = 0
        analysis_data.dependents = 0
        analysis_data.house = 0
        analysis_data.income = 0
        analysis_data.risk_questions=[0, 0, 0]
        analysis_data.vehicle = 0
        profile = InsuranceService().analysis(analysis_data)

        assert profile.auto == RiskProfileRecommendation.INELIGIBLE
        assert profile.disability == RiskProfileRecommendation.INELIGIBLE
        assert profile.home == RiskProfileRecommendation.INELIGIBLE
        assert profile.life == RiskProfileRecommendation.ECONOMIC


    def test_user_without_car_is_ineligible_for_auto(self, analysis_data):
        analysis_data.vehicle = None
        profile = InsuranceService().analysis(analysis_data)

        assert profile.auto == RiskProfileRecommendation.INELIGIBLE


    def test_user_without_house_is_ineligible_for_home(self, analysis_data):
        analysis_data.house = None
        profile = InsuranceService().analysis(analysis_data)

        assert profile.home == RiskProfileRecommendation.INELIGIBLE


    def test_user_without_income_is_ineligible_for_disability(self, analysis_data):
        analysis_data.income = 0
        profile = InsuranceService().analysis(analysis_data)

        assert profile.disability == RiskProfileRecommendation.INELIGIBLE

    def test_user_under_30_years_is_economic(self, analysis_data):
        analysis_data.age = 20
        profile = InsuranceService().analysis(analysis_data)
        
        assert profile.auto == RiskProfileRecommendation.ECONOMIC
        assert profile.disability == RiskProfileRecommendation.ECONOMIC
        assert profile.home == RiskProfileRecommendation.ECONOMIC
        assert profile.life == RiskProfileRecommendation.ECONOMIC


    def test_user_over_60_year_is_ineligible_for_disability_and_life(self, analysis_data):
        analysis_data.age = 90
        profile = InsuranceService().analysis(analysis_data)

        assert profile.disability == RiskProfileRecommendation.INELIGIBLE
        assert profile.life == RiskProfileRecommendation.INELIGIBLE

    def test_user_with_high_income(self, analysis_data):
        analysis_data.income = 300000
        profile = InsuranceService().analysis(analysis_data)

        assert profile.auto == RiskProfileRecommendation.ECONOMIC

    def test_user_house_is_mortgaged(self, analysis_data):
        analysis_data.house = HouseStatus(OwnershipStatus.MORTGAGED)
        profile = InsuranceService().analysis(analysis_data)

        assert profile.home == RiskProfileRecommendation.ECONOMIC

    def test_user_single_without_dependents(self, analysis_data):
        analysis_data.dependents = 0
        profile = InsuranceService().analysis(analysis_data)

        assert profile.life == RiskProfileRecommendation.ECONOMIC
