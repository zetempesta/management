from typing import Optional
from sqlmodel import Field, SQLModel


class StageContato(SQLModel, table=True): # type: ignore
	contato:int= Field(default=None, primary_key=True)
	prefixo:int= Field(default=None, primary_key=True)
	telefone:int= Field(default=None, primary_key=True)
	status:int