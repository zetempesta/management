from typing import Optional
from sqlmodel import Field, SQLModel


class Contact(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:str
	city:int
	cpfcnpj:Optional[str]
	neighborhood_name:Optional[str]
	flagtype:Optional[str]
	email:Optional[str]
	source:Optional[str]
	robot:Optional[str]
	sex:Optional[str]
	neighborhood:Optional[int]= Field(default=None, foreign_key="neighborhood.id")
	last_update:Optional[time]