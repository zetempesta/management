from sqlalchemy import true
from model.users.usuario import User, Login, Usersession
import uuid
from sqlmodel import select
from db.orm import select_table_first, insert, select_table_by_id, update
from fastapi import HTTPException
import datetime
from core.parameters import SESSIONTIMEOUT

def user_login(login:Login)->Usersession:
    usuario = login.usuario
    senha = login.senha
    statement = select(User).where(User.usuario == usuario).where(User.senha == senha)
    result:User
    result = select_table_first(table=Usuario, statement=statement) # type: ignore

    if result != None:
        session_id = str(uuid.uuid4())
        us = Usersession(id=session_id, user_id=result.id)
        insert(us)
        return us
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

def session_validation(user_session:str)->str:
    s:Usersession
    s = select_table_by_id(Usersession,user_session) # type: ignore
    print(user_session)
    
    if s != None :
        if s.end_time >= datetime.datetime.now():# type: ignore
            s.end_time = datetime.datetime.now() + datetime.timedelta(minutes=SESSIONTIMEOUT)
            update(s)
            return s.id
        else:
            raise HTTPException(status_code=401, detail="Sessão inválida")    
    else:
        raise HTTPException(status_code=401, detail="Sessão inválida")


