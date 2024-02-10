from typing import Optional
from sqlmodel import Field, SQLModel


class ResearchCity(SQLModel, table=True): # type: ignore
	research:int= Field(default=None, primary_key=True, foreign_key="research.id")
	city:int= Field(default=None, primary_key=True, foreign_key="city.id")