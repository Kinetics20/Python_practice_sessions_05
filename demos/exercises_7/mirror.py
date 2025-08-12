from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import requests
import time
import os

MAX_FILE_SIZE = 1024 * 1024
DELAY = 0.1


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
    time.sleep(DELAY)
    r = requests.head(url)
    if r.status_code not in range(200, 300):
        return None

    content_length = r.headers.get('content-length')
    if content_length is not None:
        content_length = int(content_length)
        if content_length >= MAX_FILE_SIZE:
            return None

    time.sleep(DELAY)
    r = requests.get(url)
    if r.status_code not in range(200, 300):
        return None

    return r.headers.get('content-type'), r.content


def handle_html(html, links_to_visit, base):
    links = [link for link in get_links(base, html) if link.netloc == base.netloc]
    for link in links:
        link = link.geturl()
        if link in visited_links:
            continue
        links_to_visit.add(link)


OUTPUT_DIR = 'output'
base_url = 'https://gynvael.coldwind.pl/?lang=pl&id=803'

# normalizacja ścieżki w base
base = urlparse(base_url)
base = base._replace(path="/" if not base.path or base.path.startswith("//") else base.path)
print('BASE', base)

visited_links = {}
links_to_visit = {base_url}

while links_to_visit:
    link = links_to_visit.pop()
    print('Visiting', link)
    res = download(link)
    if res is None:
        print('Failed to download', link)
        continue

    type_, data = res
    visited_links[link] = True

    parsed = urlparse(link)
    # jeśli brak ścieżki lub kończy się '/', dodaj index.html
    src_path = parsed.path
    if not src_path or src_path.endswith('/'):
        src_path = (src_path.rstrip('/') + '/index.html') if src_path else '/index.html'

    dst_dir = os.path.join(OUTPUT_DIR, os.path.dirname(src_path.lstrip('/')))
    assert '..' not in dst_dir
    os.makedirs(dst_dir, exist_ok=True)

    dst_file = os.path.join(OUTPUT_DIR, src_path.lstrip('/'))
    name, ext = os.path.splitext(dst_file)
    if parsed.query:
        dst_file = name + "_" + parsed.query.replace('&', '_') + ext

    assert '..' not in dst_file
    print(dst_file)
    with open(dst_file, 'wb') as f:
        f.write(data)

    if type_ is None:
        type_ = 'application/octet-stream'

    values = [v.strip() for v in type_.split(';')]
    mime_type = values[0]

    if mime_type == 'text/html':
        charset = 'utf-8'
        for param in values[1:]:
            if '=' in param:
                key, value = param.split('=', 1)
                if key.strip().lower() == 'charset':
                    charset = value.strip()

        html = data.decode(charset)
        handle_html(html, links_to_visit, base)

    print(len(visited_links), len(links_to_visit))
