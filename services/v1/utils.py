from db.orm import count_table
from fastapi import APIRouter

router = APIRouter()

@router.get("/tablesize")
async def get_research(table_name:str)->int:
    return count_table(table_name=table_name)