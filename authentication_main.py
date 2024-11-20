#This file will be updated!
#Zuri LH

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from .authentication_schemas import User, UserInDB, Token
from .authentication_databases import registered_users_database
from .authentication_utils import verifyPassword, get_password_hash, create_access_token

routerA = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authenticate/token")

@routerA.post("/register_user", response_model=User)
#register a new user profile to the application
def register_newUser(newUser: User):
    #user enters an email that is already registered
    if newUser.email in registered_users_database:
        raise HTTPException(status_code=400, detail="User already registered with that email.")
    
    #hash the password given by the user
    hashed_password = get_password_hash(newUser.password)

    #add the new user to the registered users database 
    registered_users_database[newUser.email] = UserInDB(email=newUser.email, hashed_password=hashed_password)
    
    return newUser


@routerA.post("/token", response_model=Token)
#login in registered user to the application
def login_registeredUser(userData: OAuth2PasswordRequestForm = Depends()):
    #get the registered user from the database
    registeredUser = registered_users_database.get(userData.email)

    #the info entered is not in registered user database 
    if not registeredUser or not verifyPassword(userData.password, registeredUser.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    #create an access token
    access_token = create_access_token(data={"sub": registeredUser.email})
    
    return {"access_token": access_token, "token_type": "bearer"}
