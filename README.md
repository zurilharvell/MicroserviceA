# MicroserviceA

Make sure the necessary packages have been installed:
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