from typing import Optional
from sqlmodel import Field, SQLModel


class Respondent(SQLModel, table=True): # type: ignore
	id_contact:int= Field(default=None, primary_key=True, foreign_key="contact.id")
	id_research:int= Field(default=None, primary_key=True, foreign_key="research.id")
	status_contact:Optional[int]
	dont_pickup:Optional[bool]
	dont_accept:Optional[bool]
	user_operator:Optional[int]