import json

data = {
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript", "C++"],
    "education": {
        "university": "MIT",
        "degree": "Computer Science"
    },
    "is_active": True,
    "projects": None
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Read data:")
print(loaded_data)

try:
    invalid = {"tags": {"python", "json"}}  # set
    json.dumps(invalid)
except TypeError as e:
    print("\nError during serialization unsupported file:")
    print(e)
