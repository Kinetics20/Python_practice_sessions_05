#!/usr/bin/env python3
import requests
import time
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque


class GynvaelFlagScanner:
    def __init__(self):
        self.base_url = "https://gynvael.coldwind.pl/"
        self.visited = set()
        self.to_visit = deque([self.base_url])
        self.flag_pattern = re.compile(r'HexA\{[^}]+\}')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; FlagScanner/1.0)'
        })

        self.text_extensions = {
            '.html', '.htm', '.css', '.js', '.txt', '.xml', '.json',
            '.php', '.asp', '.aspx', '.jsp', '.py', '.pl', '.sh',
            '.md', '.rst', '.log', '.cfg', '.conf', '.ini'
        }

    def is_text_file(self, url):
        """Checks if URL leads to a text file"""
        parsed = urlparse(url)
        path = parsed.path.lower()

        if '.' not in path.split('/')[-1]:
            return True

        for ext in self.text_extensions:
            if path.endswith(ext):
                return True
        return False

    def is_valid_url(self, url):
        """Checks if URL is within allowed scope"""
        parsed = urlparse(url)
        return (parsed.netloc == 'gynvael.coldwind.pl' and
                parsed.scheme == 'https')

    def extract_links(self, content, base_url):
        """Extracts all links from content"""
        links = set()

        try:
            soup = BeautifulSoup(content, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(base_url, href)
                if self.is_valid_url(full_url) and self.is_text_file(full_url):
                    links.add(full_url)

            for link in soup.find_all('link', href=True):
                href = link['href']
                full_url = urljoin(base_url, href)
                if self.is_valid_url(full_url) and self.is_text_file(full_url):
                    links.add(full_url)

            for script in soup.find_all('script', src=True):
                src = script['src']
                full_url = urljoin(base_url, src)
                if self.is_valid_url(full_url) and self.is_text_file(full_url):
                    links.add(full_url)

        except Exception as e:
            print(f"Error parsing HTML: {e}")

        url_pattern = re.compile(r'https://gynvael\.coldwind\.pl/[^\s"\'<>]+')
        regex_links = url_pattern.findall(content)

        for link in regex_links:
            if self.is_valid_url(link) and self.is_text_file(link):
                links.add(link)

        return links

    def search_for_flag(self, content):
        """Searches for flag in content"""
        matches = self.flag_pattern.findall(content)
        return matches

    def fetch_url(self, url):
        """Fetches URL content with error handling"""
        try:
            print(f"Checking: {url}")
            response = self.session.get(url, timeout=10)

            content_type = response.headers.get('content-type', '').lower()
            if any(t in content_type for t in
                   ['text/', 'application/javascript', 'application/json', 'application/xml']):
                return response.text
            elif 'html' in content_type:
                return response.text
            else:
                print(f"  Skipped - not a text file: {content_type}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def scan(self):
        """Main scanning loop"""
        print("Starting scan of Gynvael's blog...")
        print("Looking for flag starting with 'HexA{'")
        print("-" * 50)

        while self.to_visit:
            current_url = self.to_visit.popleft()

            if current_url in self.visited:
                continue

            self.visited.add(current_url)

            content = self.fetch_url(current_url)
            if not content:
                time.sleep(1)
                continue

            flags = self.search_for_flag(content)
            if flags:
                print("\n" + "=" * 60)
                print("🎉 FLAG FOUND! 🎉")
                print(f"URL: {current_url}")
                for flag in flags:
                    print(f"Flag: {flag}")
                print("=" * 60)
                return flags[0]

            new_links = self.extract_links(content, current_url)
            for link in new_links:
                if link not in self.visited:
                    self.to_visit.append(link)

            print(f"  Found {len(new_links)} new links")
            print(f"  Visited: {len(self.visited)}, To check: {len(self.to_visit)}")

            time.sleep(1)

        print("\n" + "=" * 50)
        print("Scan completed. No flag found.")
        print(f"Checked {len(self.visited)} URLs total")
        return None


def main():
    scanner = GynvaelFlagScanner()

    try:
        flag = scanner.scan()
        if flag:
            print(f"\nFound flag: {flag}")
        else:
            print("\nFailed to find flag.")
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
        print(f"Checked {len(scanner.visited)} URLs before interruption.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
