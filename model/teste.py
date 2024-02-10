from typing import Optional
from sqlmodel import Field, SQLModel


class Teste(SQLModel, table=True): # type: ignore
	texto:Optional[str]