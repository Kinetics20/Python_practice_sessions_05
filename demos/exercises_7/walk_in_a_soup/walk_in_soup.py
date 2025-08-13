from bs4 import BeautifulSoup
import hashlib

hashes = [
    "a089270cf8885f7708217f3b0d5e0dfea3bd20f453206d69152e7087e49da710",
    "60694ade51c5dab750f2254861d355050ec67fc5a1a3d0ede3020b93747bf93f",
    "eb81cb469b3c5ab17375b82f27bbfb11c19c929fcf506158aebf6921366ebefe",
    "7f415ab5ea23db8f6eeefc85aa9200daff69b0a0b21e8ee75c31b8926ff4b9e4",
    "a0c683bb3a39a0f4cb7c03f33a01b4dc61f4e98c05cd3680ab24189502fba8b3",
    "5f16027d0fb8c6c5149cbc5ab34199db98298bfc754f3458f2dd8215fee113bb",
    "88859b8592ae10ef2cbc9a815bfde74ce531335babef5a558ccfe8af6079f0aa",
    "eeb421725c5c356e60b3844a4f0261b9de095353e1cb1764074531c98ac5d3a6",
    "e1b92ea9d45c8796aa3b5d032c12038f3298fb8654dd2ab0649ade673b972c70"
]

with open("whatthe.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

found = {}

for tag in soup.find_all(True):

    for attr, val in tag.attrs.items():

        if isinstance(val, list):
            val = " ".join(val)
        h = hashlib.sha256(val.encode()).hexdigest()
        if h in hashes:

            if tag.contents:
                last_child = tag.contents[-1]
                if hasattr(last_child, "attrs"):  # to też tag
                    for a2, v2 in last_child.attrs.items():
                        if isinstance(v2, list):
                            v2 = " ".join(v2)
                        found[h] = v2

flag = "".join(found[h] for h in hashes)
print(flag)
