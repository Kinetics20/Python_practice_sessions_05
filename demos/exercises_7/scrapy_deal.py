import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

START_URL = "https://gynvael.coldwind.pl/"
VISITED = set()

BINARY_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico",
    ".zip", ".rar", ".7z", ".pdf", ".exe", ".dll", ".so",
    ".mp3", ".mp4", ".avi", ".mov", ".webm", ".woff", ".woff2"
}


def is_binary_url(url):
    path = urlparse(url).path.lower()
    for ext in BINARY_EXT:
        if path.endswith(ext):
            return True
    return False


def crawl(url):
    if url in VISITED or is_binary_url(url):
        return None
    VISITED.add(url)

    try:
        time.sleep(1)
        r = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"[ERR] {url} -> {e}")
        return None

    text = r.text

    if "HexA{" in text:
        print(f"[FLAG FOUND] {url}")
        print(text)
        return text

    content_type = r.headers.get("Content-Type", "")
    if "text/html" in content_type or url.endswith(".html") or url == START_URL:
        soup = BeautifulSoup(text, "html.parser")
        for a in soup.find_all("a", href=True):
            next_url = urljoin(url, a["href"])

            parsed = urlparse(next_url)
            if parsed.scheme == "https" and parsed.netloc == "gynvael.coldwind.pl":
                result = crawl(next_url)
                if result is not None:
                    return result
    return None


if __name__ == "__main__":
    crawl(START_URL)
