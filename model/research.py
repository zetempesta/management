from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date


class Research(SQLModel, table=True): # type: ignore
	name:str
	begin_date:date
	end_date:date
	id:int= Field(default=None, primary_key=True)
	valid:bool
	meta:int