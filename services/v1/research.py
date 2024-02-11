from fastapi import APIRouter
from controller.research import list_research
from model.research import Research 
from core.parameters import PAGE_SIZE

router = APIRouter()

@router.get("/researchs", response_model=list[Research])
async def get_researchs():
    return list_research()