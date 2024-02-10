from typing import Optional
from sqlmodel import Field, SQLModel


class Neighborhood(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:str
	city:int= Field(default=None, foreign_key="city.id")
	region:Optional[str]