import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.post(f"{BASE_URL}/users",json= {
    "username": "testuser",
    "email": "test@example.com",
    "password": "test1234"
})
print("POST /users? =>", response.status_code, response.json())

response = requests.get(f"{BASE_URL}/users/")
print("GET /users/ =>", response.status_code, response.json())