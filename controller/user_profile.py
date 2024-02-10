from model.users.user_profile import UserProfile
from sqlmodel import select
from db.orm import select_table

def validate_permission(id_user:int, id_profile:int)->bool:
    stmt = select(UserProfile).where(UserProfile.id_user == id_user).where(UserProfile.id_profile == id_profile)
    result = select_table(table=UserProfile, statement=stmt)
    
    if result != None:
        return True
    else:
        return False