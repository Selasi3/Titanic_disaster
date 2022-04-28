from enum import Enum
from typing import List
from pydantic import BaseModel


class Journey(str, Enum):
    Chereborg = "Cherborg"
    Queenstown = "Queenstown"
    Southampthon = "Southampthon"
    
class Gender(str, Enum):
    Male = "Male",
    Female = "Female"

class ModelInput(BaseModel):
    pclass: int
    sex: Gender
    age: int 
    sibsp: int
    parch: int
    fare: float
    embarked: Journey 