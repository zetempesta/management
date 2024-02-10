from typing import Optional
from sqlmodel import Field, SQLModel


class ContactPhone(SQLModel, table=True): # type: ignore
	contact:int= Field(default=None, primary_key=True, foreign_key="contact.id")
	phone:int= Field(default=None, primary_key=True, foreign_key="phone.id")
	status:str