from sqlalchemy import Null
from sqlmodel import select
from db.orm import insert, select_table, select_table_by_id, delete, update, select_table_first
from model.research import Research
from model.survey import Survey
from model.research_survey import Research_Survey
from core.parameters import PAGE_SIZE

def list_research()->list[Research]:
    return_value:list[Research]
    return_value = select_table(Research) # type: ignore

    return return_value

# def list_research_text_filter(offset:int, limit:int=PAGE_SIZE)->list[Research]:
#     return_value:list[Research] = Null

#     return return_value

def get_Research(id:int)->Research:
    return_value:Research
    return_value = select_table_by_id(table=Research, id=id) # type: ignore

    return return_value

def insert_research(item:Research)->bool:
    item = insert(item)
    s = Survey(name=item.name, id=item.id)
    insert(s)
    rs = Research_Survey(research=item.id,survey=item.id, order_survey=1)
    insert(rs)
    
    return True

def delete_research(item:Research)->bool:
    delete(item)
    s = select_table_by_id(Survey, item.id)
    delete(s)
    stmt = select(Research_Survey).where(Research_Survey.survey == item.id).where(Research_Survey.research == item.id)
    rs = select_table_first(Research_Survey, stmt)
    delete(rs)
    return True

def update_research(item:Research)->bool:
    update(item)
    
    return True
