import requests


data = {
    "username": "holo155",
    "password": "65655",
}

res = requests.post(
    url="http://127.0.0.1:8000/get-info-user",
    data=data
)

print(res.json())