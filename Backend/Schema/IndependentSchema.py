from datetime import datetime
from typing import Optional, List
from Schema.DependentSchema import *
from pydantic import BaseModel


class Role(BaseModel):
    Role_ID: Optional[int] = None
    Role_Name: str
    Role_Description: str
    Active: bool
    Skills: List["Skill"]
    LearningJourneys: List["LearningJourney"]
    # Skills:


class Skill(BaseModel):
    Skill_ID: Optional[int] = None
    Skill_Name: str
    Skill_Description: str
    Active: bool
    Roles: List[Role]
    Course: List["Course"]
    LearningJourneys: List["LearningJourney"]

class Course(BaseModel):
    Course_ID: Optional[str] = None
    Course_Name: str
    Course_Desc: str
    Course_Status: str
    Course_Type: str
    Course_Category: str
    Skills: List[Skill]
    LearningJourneys: List["LearningJourney"]

class UserRole(BaseModel):
    Role_ID: Optional[int] = None
    Role_Name: str