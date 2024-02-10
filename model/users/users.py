from typing import Optional
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	mail:str
	name:str
	username:str
	password:str
	active:Optional[bool]