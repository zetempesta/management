from typing import Optional
from sqlmodel import Field, SQLModel


class CountryState(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	name:Optional[str]
	uf:Optional[str]
	ibge:Optional[int]
	country:Optional[int]
	ddd:Optional[]