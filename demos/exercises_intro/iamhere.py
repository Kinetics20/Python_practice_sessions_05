import base64

encoded = "SGV4QXJjYW5he3ByYWt0eWN6bnktcHl0aG9uLW1hai0yMDI1"
decoded = base64.b64decode(encoded).decode("utf-8")

print(decoded)