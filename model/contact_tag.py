from typing import Optional
from sqlmodel import Field, SQLModel


class ContactTag(SQLModel, table=True): # type: ignore
	id_contact:int= Field(default=None, primary_key=True)
	key:str= Field(default=None, primary_key=True)
	value:str