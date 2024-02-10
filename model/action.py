from typing import Optional
from sqlmodel import Field, SQLModel


class Action(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:str