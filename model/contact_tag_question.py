from typing import Optional
from sqlmodel import Field, SQLModel


class ContactTagQuestion(SQLModel, table=True): # type: ignore
	id_research:int= Field(default=None, primary_key=True)
	id_question:int= Field(default=None, primary_key=True)
	tag:str= Field(default=None, primary_key=True)