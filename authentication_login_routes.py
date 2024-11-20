#This file will be updated!
#Zuri LH

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#from typing import List
from authentication_schemas import User, UserInDB, Token
from authentication_databases import registered_users_database
from authentication_utils import verifyPassword, get_password_hash, create_access_token, decode_access_token

authentication_app = FastAPI()
#routerA = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@authentication_app.post("/register_user", response_model=User)
#register a new user profile to the application
def register_newUser(newUser: User):
    #user enters an email that is already registered
    if newUser.email in registered_users_database:
        raise HTTPException(status_code=400, detail="This email is already registered a User")
    
    #hash the password given by the user
    hashed_password = get_password_hash(newUser.password)

    #add the new user to the registered users database 
    registered_users_database[newUser.email] = UserInDB(email=newUser.email, hashed_password=hashed_password)
    
    return newUser


@authentication_app.post("/token", response_model=Token)
#login in registered user to the application
def login_registeredUser(login_form_data: OAuth2PasswordRequestForm = Depends()):
    #get the registered user from the database
    registeredUser = registered_users_database.get(login_form_data.email)

    #the info entered is not in registered user database 
    if not registeredUser or not verifyPassword(login_form_data.password, registeredUser.hashed_password):
        raise HTTPException(status_code=400, detail="The username or password you entered is invalid")
    
    #create an access token
    access_token = create_access_token(data={"sub": registeredUser.email})
    
    return {"access_token": access_token, "token_type": "bearer"}
