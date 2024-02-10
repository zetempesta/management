from typing import Optional
from sqlmodel import Field, SQLModel


class Question(SQLModel, table=True): # type: ignore
	wording:str
	id:int= Field(default=None, primary_key=True)
	survey:int= Field(default=None, foreign_key="survey.id")
	order_question:int
	formtype:str= Field(default=None, foreign_key="formtype.formtype")
	null_answer:str