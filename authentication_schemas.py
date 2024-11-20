#This will be updated!
#Zuri LH

from pydantic import BaseModel
from typing import List, Optional

#the email will serve has the username
class User(BaseModel):
    email: str
    password: str
    #liked_movies: Optional[List[int]] = []

class UserInDB(User):
    hashed_password: str
    #liked_movies: Optional[List[int]] = []

class Token(BaseModel):
    access_token: str
    token_type: str

