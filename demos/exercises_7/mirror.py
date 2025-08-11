from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

MAX_FILE_SIZE = 1024 * 1024

def has_link(tag):
    return 'href' in tag.attrs or 'src' in tag.attrs

def get_links(base, html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(has_link)

    links = []
    for t in tags:

        for attr in ['href', 'src']:
            link = t.attrs.get(attr)
            if link is not None:
                links.append(link)

    final_links = []
    for link in links:
        link = urlparse(link)
        if link.netloc == '':
            link = link._replace(netloc=base.netloc)

        if link.scheme == '':
            link = link._replace(scheme=base.scheme)

        if not link.path.startswith('/'):

            new_path = base.path
            if not new_path.endswith('/'):
                new_path += '/'

            new_path += link.path

            link = link._replace(path=new_path)

        if link.fragment:
            link = link._replace(fragment='')

        final_links.append(link)

    return final_links

def download(url):
    r = requests.head(url)
    if r.status_code not in range(200, 300):
        return None

    content_length = r.headers.get('content-length')
    if content_length is not None:
        content_length = int(content_length)
        if content_length >= MAX_FILE_SIZE:
            return None

    r = requests.get(url)
    if r.status_code not in range(200, 300):
        return None

    return r.headers.get('content-type'), r.content


url = 'https://gynvael.coldwind.pl//?lang=pl&id=803'
print(download(url))
exit()

base = urlparse(url)
print('BASE', base)
visited_links = {}
links_to_visit = set()


with open('example.html', encoding='utf-8') as f:
    html = f.read()
    links = [link for link in get_links(base, html) if link.netloc == base.netloc]

    for link in links:
        link = link.geturl()
        if link in visited_links:
            continue

        links_to_visit.add(link)

print(links_to_visit)