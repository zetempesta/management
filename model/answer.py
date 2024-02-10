from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime as dt


class Answer(SQLModel, table=True): # type: ignore
	research:int= Field(default=None, primary_key=True, foreign_key="research.id")
	question:int= Field(default=None, primary_key=True, foreign_key="question.id")
	date_time_start:dt
	date_time_end:Optional[dt]
	contato:int= Field(default=None, primary_key=True, foreign_key="contact.id")
	answer:str