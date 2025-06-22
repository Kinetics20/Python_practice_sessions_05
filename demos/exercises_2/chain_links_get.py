import requests

url = "https://py10-day2-577570284557.europe-west1.run.app/ex1"

while url:
    response = requests.get(url)
    data = response.json()
    print(data)

    url = data.get("next_url")
