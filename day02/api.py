import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

for key,value in response.json().items():
    if key == "title":
        print("Title is:", value)
    elif key == "completed":
        print("Completed Status is:", value)