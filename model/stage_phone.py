from typing import Optional
from sqlmodel import Field, SQLModel


class StagePhone(SQLModel, table=True): # type: ignore
	id:Optional[int]
	prefixo:Optional[int]
	telefone:Optional[int]
	phone_number:Optional[str]
	phone_correct:Optional[str]