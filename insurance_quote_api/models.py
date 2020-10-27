from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator

from enum import Enum
from typing import List, Optional
from datetime import date
from dataclasses import dataclass


class MaritalStatus(str, Enum):
    """Enum, can be single or married."""
    SINGLE: str = "single"
    MARRIED: str = "married"


class OwnershipStatus(str, Enum):
    """Enum, can be owned or mortgaged."""
    OWNED: str = "owned"
    MORTGAGED: str = "mortgaged"

class RiskProfileRecommendation(str, Enum):
    """Enum, can be economic, regular, responsible or ineligible."""
    ECONOMIC: str = "economic"
    REGULAR: str = "regular"
    RESPONSIBLE: str = "responsible"
    INELIGIBLE: str = "ineligible"

@dataclass
class HouseStatus:
    """@dataclass with optional field. Can only have max one house, with ownership status, or zero."""
    ownership_status: OwnershipStatus


@dataclass
class VehicleData:
    """@dataclass with optional field. Can only have max one vehicle, with year, or zero."""
    year: int

    def years_old(self):
        """Returns current year minus vehicle year"""
        return date.today().year - self.year


@dataclass
class UserData:
    """@dataclass with user input data."""
    age: int
    dependents: int
    house: Optional[HouseStatus]
    income: int
    marital_status: MaritalStatus
    risk_questions: List[int]
    vehicle: Optional[VehicleData]

    def base_score(self):
        """Returns sum of self.risk_questions"""
        return sum(self.risk_questions)


@dataclass
class RiskProfilePlan:
    """@dataclass with insurance plans and respective recommendation for the user."""
    auto: RiskProfileRecommendation
    disability: RiskProfileRecommendation
    home: RiskProfileRecommendation
    life: RiskProfileRecommendation