from typing import Optional
from sqlmodel import Field, SQLModel


class Survey(SQLModel, table=True): # type: ignore
	name:str
	id:int= Field(default=None, primary_key=True)