from typing import Optional
from sqlmodel import Field, SQLModel


class ResearchUser(SQLModel, table=True): # type: ignore
	id_research:int= Field(default=None, primary_key=True, foreign_key="research.id")
	id_user:int= Field(default=None, primary_key=True, foreign_key="users.id")