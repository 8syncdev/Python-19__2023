from requests.api import get


data = get("https://jsonplaceholder.typicode.com/posts")

print(list(data))