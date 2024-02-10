from typing import Optional
from sqlmodel import Field, SQLModel


class UserProfile(SQLModel, table=True): # type: ignore
	id_user:int= Field(default=None, primary_key=True, foreign_key="users.id")
	id_profile:int= Field(default=None, primary_key=True, foreign_key="profile.id")