from typing import Optional
from sqlmodel import Field, SQLModel


class Phone(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	prefixo:Optional[int]
	telefone:Optional[int]
	phone_number:str
	valid:bool