from typing import Optional
from sqlmodel import Field, SQLModel


class SchemaMigrations(SQLModel, table=True): # type: ignore
	version:str= Field(default=None, primary_key=True)