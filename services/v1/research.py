from fastapi import APIRouter
from controller.research import insert_research, list_research
from model.research import Research 
from core.parameters import PAGE_SIZE

router = APIRouter()

@router.get("/research", response_model=list[Research])
async def get_research():
    return list_research()

@router.post("/research")
async def post_research(research:Research)->bool:
    return insert_research(research)