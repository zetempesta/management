from typing import Optional
from sqlmodel import Field, SQLModel


class Formtype(SQLModel, table=True): # type: ignore
	formtype:str= Field(default=None, primary_key=True)
	name:Optional[str]