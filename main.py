from fastapi import FastAPI
import services.v1.research as research
import services.v1.utils as utils
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research.router)
app.include_router(utils.router)
