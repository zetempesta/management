from typing import Optional
from sqlmodel import Field, SQLModel


class ResearchSurvey(SQLModel, table=True): # type: ignore
	research:int= Field(default=None, primary_key=True, foreign_key="research.id")
	survey:int= Field(default=None, primary_key=True, foreign_key="survey.id")
	order_survey:int