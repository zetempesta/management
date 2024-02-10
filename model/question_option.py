from typing import Optional
from sqlmodel import Field, SQLModel


class QuestionOption(SQLModel, table=True): # type: ignore
	title:str
	value:str
	question:int= Field(default=None, foreign_key="question.id")
	id:int= Field(default=None, primary_key=True)
	option_order:int