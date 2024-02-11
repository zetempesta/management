from sqlalchemy import Null
from db.orm import insert, select_table, select_table_by_id, delete, update
from model.research import Research
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
    insert(item)
    
    return True

def delete_research(item:Research)->bool:
    delete(item)
    
    return True

def update_research(item:Research)->bool:
    update(item)
    
    return True
