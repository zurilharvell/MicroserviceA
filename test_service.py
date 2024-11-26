import requests

BASE_URL = "http://127.0.0.1:8000"

def make_post_request(endpoint, payload, headers=None):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def test_register_user(user_email, user_password):
    payload = {"email": user_email, "password": user_password}
    return make_post_request("/register_user", payload)

def test_login_user(user_email, user_password):
    payload = {"username": user_email, "password": user_password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return make_post_request("/token", payload, headers)

def main():
    test_email = "zurilh28@gmail.com"
    test_password = "threatLEVELm1dn1ght"

    print("Creating a new user profile with the info entered.")
    registered = test_register_user(test_email, test_password)
    print(registered)

    print("Logging in a registered user")
    login = test_login_user(test_email, test_password)
    print(login)

    login_token = login.get("access_token")
    print(f"Login token: {login_token}")
    print("This is the end of the test.")

if __name__ == "__main__":
    main()
