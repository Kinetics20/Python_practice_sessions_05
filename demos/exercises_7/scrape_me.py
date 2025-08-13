import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

START_URL = "https://py10-day7-577570284557.europe-west1.run.app/ex3/"
VISITED = set()


def crawl(url):
    if url in VISITED:
        return None
    VISITED.add(url)

    try:
        r = requests.get(url, timeout=5)
    except requests.RequestException as e:
        print(f"Error during: {url}: {e}")
        return None

    text = r.text

    if "HexA{" in text:
        print(f"[FLAG FOUND] {url}")
        print(text)
        return text

    soup = BeautifulSoup(text, "html.parser")

    for a in soup.find_all("a", href=True):
        next_url = urljoin(url, a["href"])
        result = crawl(next_url)
        if result is not None:
            return result

    return None


if __name__ == "__main__":
    crawl(START_URL)
