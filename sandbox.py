import sqlalchemy
from sqlmodel import select
from db.orm import select_table
from model.research import Research
from controller.research import list_research
from sqlalchemy.sql.operators import ilike_op,like_op



stmt = select(Research).where(ilike_op(Research.c, f'h%'))

print(select_table(Research, stmt))