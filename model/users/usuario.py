from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime as dt
import datetime
from pydantic import BaseModel
from core.parameters import SESSIONTIMEOUT


class User(SQLModel, table=True): # type: ignore
	id:int= Field(default=None, primary_key=True)
	email:str
	nome:str
	usuario:str
	senha:str
	data_hora_criaca:dt
	ultima_atualizacao:dt
	data_hora_criacao:Optional[dt]
	usuario_criacao:Optional[int]= Field(default=None, foreign_key="usuario.id")
	data_hora_atualizacao:Optional[dt]
	usuario_atualizacao:Optional[int]= Field(default=None, foreign_key="usuario.id")

class Login(BaseModel):
	usuario:str
	senha:str

class Usersession(SQLModel, table=True): # type: ignore
	id:str= Field(default=None, primary_key=True)
	user_id:int
	start_time:Optional[dt]=dt.now()
	end_time:Optional[dt]=dt.now() + datetime.timedelta(minutes=SESSIONTIMEOUT)

