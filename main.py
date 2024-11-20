import uvicorn
from authentication_login_routes import authentication_app

if __name__ == "__main__":
    uvicorn.run(authentication_app, host="127.0.0.1", port=8000)