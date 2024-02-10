from fastapi import APIRouter
from controller.research import list_research
from model.research import Research 
from core.parameters import PAGE_SIZE

router = APIRouter()

@router.get("/researchs", response_model=list[Research])
async def get_research(offset:int, limit:int=PAGE_SIZE):
    return list_research(offset=offset, limit=limit)