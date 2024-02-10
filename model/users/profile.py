from typing import Optional
from sqlmodel import Field, SQLModel


class Profile(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:str
	tag:Optional[str]