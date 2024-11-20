# MicroserviceA

About Microservice:
A microservice for handling user login authentication. This service validates user credentials and returns authentication tokens.

Key Features of Microservice:
1. user login with email and password
2. token based authentication
3. error handling for invalid login credentials

How to Install Microservice:
1. Clone the Repo
git clone https://github.com/zurilharvell/MicroserviceA.git
cd MicroserviceA

2. Install required dependencies 
pip install fastapi
pip install uvicorn
pip install PyJWT
pip install passlib
pip install python-mulipart
pip install requests


First start running the server in 1 terminal: 
uvicorn main:authentication_app --reload

In a separate terminal run the test program:
python3 test_service.py
