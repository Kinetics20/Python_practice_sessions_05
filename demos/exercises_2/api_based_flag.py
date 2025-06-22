import requests

BASE_URL = "https://py10-day2-577570284557.europe-west1.run.app"

tables_resp = requests.get(f"{BASE_URL}/ex5/get-tables")
tables = tables_resp.json()
print("Tables:", tables)

flag_chars = []

if "flag" in tables:
    table = "flag"
    print(f"\n🔍 Searching table: {table}")

    cols_resp = requests.post(f"{BASE_URL}/ex5/get-columns", json={"table": table})
    columns = cols_resp.json()
    print(f"  Columns: {columns}")

    rowcount_resp = requests.post(f"{BASE_URL}/ex5/get-row-count", json={"table": table})
    row_count = rowcount_resp.json().get("row_count", 0)
    print(f"  Row count: {row_count}")

    for row in range(row_count):
        char_payload = {
            "table": table,
            "row": row,
            "column": "character"
        }
        index_payload = {
            "table": table,
            "row": row,
            "column": "index"
        }

        char_resp = requests.post(f"{BASE_URL}/ex5/get-entry", json=char_payload)
        index_resp = requests.post(f"{BASE_URL}/ex5/get-entry", json=index_payload)

        char = char_resp.json().get("entry", "")
        index = index_resp.json().get("entry", -1)

        flag_chars.append((index, char))

    sorted_chars = sorted(flag_chars, key=lambda x: x[0])
    flag = "".join(char for _, char in sorted_chars)

    print("\n🚩 FLAG:", flag)
else:
    print("❌ 'flag' table not found!")
