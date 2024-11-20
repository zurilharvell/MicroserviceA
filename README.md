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

Request Data:
- Send a POST request to the /token endpoint with the user’s email and password
- Review the test_registerUser function in the test_service.py for an example

Receive Data:
- Handle the JSON response returned by the POST request
- Review the test_login_regUser function in the test_service.py for an example

Terminal 1:
uvicorn main:authentication_app --reload

Terminal 2:
python3 test_service.py

<img width="714" alt="Screenshot 2024-11-20 at 3 00 00 AM" src="https://github.com/user-attachments/assets/212a4480-4d93-40e7-bb92-3365b8ba0d8a">



