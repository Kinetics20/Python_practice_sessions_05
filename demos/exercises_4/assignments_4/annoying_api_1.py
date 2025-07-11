import requests
import hashlib
import os

resp = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
data = resp.json()
challenge_hex = data["challenge"]
challenge = bytes.fromhex(challenge_hex)

while True:
    suffix = os.urandom(8)
    token = challenge + suffix
    hash_ = hashlib.sha256(token).hexdigest()
    if hash_.startswith('ffffff'):
        print("[+] Found suffix:", suffix.hex())
        break

pow_token = (challenge + suffix).hex()
flag_resp = requests.get(
    "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-flag",
    params={"pow": pow_token}
)
print("🏁 Flag:", flag_resp.text)
