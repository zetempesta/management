from typing import Optional
from sqlmodel import Field, SQLModel


class City(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:str
	initials:str
	country_state:int= Field(default=None, foreign_key="country_state.id")