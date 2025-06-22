import requests

url = "https://py10-day2-577570284557.europe-west1.run.app/ex3"
secret = ""

while True:
    headers = {"X-Secret": secret} if secret else {}

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Response is not a valid JSON.")
        print("Status code:", response.status_code)
        print("Response content:", response.text)
        break

    print(data)

    if "flag" in data:
        print("🎉 FLAG:", data["flag"])
        break

    secret = data.get("next_secret")

    if not secret:
        print("❌ No next_secret found — stopping.")
        break
