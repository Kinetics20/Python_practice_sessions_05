import requests
import os

BASE_URL = "https://py10-day6-577570284557.europe-west1.run.app/ex2/"
WORDLIST_FILE = "httpwalk-dict.txt"
TIMEOUT = 5
MAX_DEPTH = 5


def load_words(path):
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def try_request(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code == 200:
            return response
    except requests.RequestException:
        pass
    return None


def recursive_walk(path_parts, wordlist, depth):
    if depth > MAX_DEPTH:
        return None

    for word in wordlist:
        new_path_parts = path_parts + [word]
        dir_url = BASE_URL + "/".join(new_path_parts) + "/"

        response = try_request(dir_url)
        if response:
            print(f"[📁] DIR: {dir_url}")

            flag_url = dir_url + "flag.txt"
            flag_resp = try_request(flag_url)
            if flag_resp and "flag" in flag_resp.text.lower():
                print(f"[🚩] FLAG FOUND: {flag_url}")
                print(flag_resp.text.strip())
                return flag_resp.text.strip()

            result = recursive_walk(new_path_parts, wordlist, depth + 1)
            if result:
                return result

        file_url = BASE_URL + "/".join(path_parts + [word + ".txt"])
        file_resp = try_request(file_url)
        if file_resp and "flag" in file_resp.text.lower():
            print(f"[🚩] FLAG FOUND: {file_url}")
            print(file_resp.text.strip())
            return file_resp.text.strip()

    return None


if __name__ == "__main__":
    print("[🚀] Scanning paths recursively...")
    wordlist = load_words(WORDLIST_FILE)
    flag = recursive_walk([], wordlist, 0)

    if not flag:
        print("[❌] Flag not found.")
