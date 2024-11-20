import requests

BASE_URL = "http://127.0.0.1:8000"

def test_registerUser(user_email, user_password):
    test_url = f"{BASE_URL}/register_user"

    decoding_payload = {"email": user_email, "password": user_password}

    sys_response = requests.post(test_url, json=decoding_payload)
    #print("This is a response:", sys_response.text)

    return sys_response.json()

def test_login_regUser(user_email, user_password):
    test_url = f"{BASE_URL}/token"

    decoding_payload = {"username": user_email, "password": user_password}

    headers = {"Content-Type": "login-application/x-www-form-urlencoded"}

    sys_response = requests.post(test_url, data=decoding_payload, headers=headers)
    print("This is a response:", sys_response.text)

    return sys_response.json()

def main():
    #Register a new user
    test_email = "zurilh28@gmail.com"
    test_password = "threatLEVELm1dn1ght"

    print("Creating a new user profile with the info entered.")
    #the reponse from the request
    registered = test_registerUser(test_email, test_password)
    #print the response
    print(registered)

    #Login & Get a Token
    print("Logging in a registered user")
    #get the login reponse 
    login = test_login_regUser(test_email, test_password)
    print(login)
    login_token = login.get("access_token")
    print("This is the end of the test.")


if __name__ == "__main__":
    main()