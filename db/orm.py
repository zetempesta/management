from sqlalchemy import text
from sqlmodel import Session, select
from db.pg import engine



def insert(item):
    s = Session()
    with Session(engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)
            return item

def count_table(table_name:str)->int:
    cur = engine.connect().execute(text(f"""select count(*) from {table_name}"""))
    recset = cur.fetchall()
    registros = []
    for rec in recset:
      registros.append(rec)
    return registros[0][0]

def select_table_offset(table,limit:int, offset:int):

    with Session(engine) as session:
        statement = select(table).limit(limit=limit).offset(offset=offset)
        return session.exec(statement).fetchall()

def select_table(table,statement=None):

    with Session(engine) as session:
        if statement == None:
            statement = select(table)
        return session.exec(statement).fetchall()

def select_table_by_id(table,id):
    with Session(engine) as session:
        return session.get(table,id)    

def select_table_first(table,statement=None):
    with Session(engine) as session:
        if statement == None:
            statement = select(table)
        
        value = session.exec(statement=statement).one_or_none()
        return value
    
def update(record):
    with Session(engine) as session:
        session.add(record)
        session.commit()
        session.refresh(record)

def delete(record):
    with Session(engine) as session:
        session.delete(record)
        session.commit()


        
