from typing import Optional
from sqlmodel import Field, SQLModel


class Research_Survey(SQLModel, table=True): # type: ignore
	research:int= Field(default=None, primary_key=True)
	survey:int= Field(default=None, primary_key=True)
	order_survey:int