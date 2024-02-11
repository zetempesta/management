import sqlalchemy
from sqlmodel import select
from db.orm import select_table, insert
from model.survey import Survey
from model.research_survey import Research_Survey


s=Survey(name='Ufa',id=69)
sr = Research_Survey(research=69, survey=69, order_survey=1)
insert(s)
insert(sr)
