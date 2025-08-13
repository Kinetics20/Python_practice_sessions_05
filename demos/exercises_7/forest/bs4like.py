# Don't look here unless you really really want to.
# The exercise is in forest.py.

import hashlib

ENCRYPTED_FLAG = (
    "04a39790ecbb0771cb1bbd11f5f0e877df2d31162d8c87651c58e40f3feb"
    "3f60ececb162ecc450a09d8675c504b7ec2dd1f6bcfca047695f53a09ca3"
)

ENCRYPTED_SECRET1 = "d69bf7b5083465ae3d76fcd6af2a8df72fe11c1021e847bee79e8a4aac638165750eeca8b6ed2d7791ee435e5fb49c41704cf04b176d2634f19cb19ebdea8448"
ENCRYPTED_SECRET2 = "82acc6ec7d1294cd2fd0d16a3a722f4f3f76c99be2f6da78f5d5caac95e597c567fe2bc60fabc29c9638ff264f1d6073f940c251c874e3d4d5bcfca1b39f6ff0"
ENCRYPTED_SECRET3 = "8bbd8a37d7fdd52ad96f3ba13ab6913019abc01fa39ce6235960da753bfd304bd8599bdcfb80db9f2e5e4f3bfc716cbb87399b8efa6afd5a33cc32368690bc5c"
ENCRYPTED_SECRET4 = "4229b9e3d15fb68c068aee471d0b92debee9ac775fc9377a3ab5304863afac6b6c252b5a1dd13623c719aa178298fc84440c8f68c5c1182377f9087ed477e1a7"

def xor(bytes_a, bytes_b):
  return bytes([a ^ b for a, b in zip(bytes_a, bytes_b)])

class Tag:
  def __init__(self, name, children, secret=None):
    self.name = name
    self.attrs = {}
    self.contents = children
    self.children = iter(children)
    self.parent = None
    self.next_sibling = None
    self.previous_sibling = None
    self._secret = secret
    self._ordinal = 0

    for i, child in enumerate(children):
      child.parent = self
      child.previous_sibling = children[i-1] if i > 0 else None
      child.next_sibling = children[i+1] if i < len(children)-1 else None
      child._ordinal = i

  def __str__(self):
    return self._str_worker()

  def _str_worker(self, level=0):
    """
    Recursively generates a string representation of the tree.
    """
    output = []
    output.append(" " * (level * 2))
    output.append(f"<{self.name}")

    if self._secret:
      output.append(f" SECRET-IS-HERE-CALL-.secret()-ON-ME")

    output.append(">")

    if not self.contents:
      output.append(f"</{self.name}>\n")
      return "".join(output)

    output.append("\n")
    for child in self.contents:
      output.append(child._str_worker(level + 1))

    output.append(" " * (level * 2))
    output.append(f"</{self.name}>\n")

    return "".join(output)

  def __repr__(self):
    return self.__str__()

  def _get_ordinal(self):
    ordinal = [f"{self._ordinal}:{self.name}"]
    node = self.parent
    while node:
      ordinal.insert(0, f"{node._ordinal}:{node.name}")
      node = node.parent

    return ".".join(ordinal)

  def secret(self):
    if self._secret:
      key = hashlib.sha512(self._get_ordinal().encode()).digest()
      secret = bytes.fromhex(self._secret)
      assert len(key) == len(secret)

      decrypted = xor(key, secret)
      assert decrypted.startswith(b"\xff\xff\xff\xff"), "? Trying sth funny?"

      return decrypted[4:]
    else:
      return "Secret is not here."

def print_decrypted_flag(secret1, secret2, secret3, secret4):
  good = True

  if secret1 is None:
    print("Secret 1 was not provided.")
    good = False

  if secret2 is None:
    print("Secret 2 was not provided.")
    good = False

  if secret3 is None:
    print("Secret 3 was not provided.")
    good = False

  if secret4 is None:
    print("Secret 4 was not provided.")
    good = False

  if not good:
    return

  key = xor(secret1, secret2)
  key = xor(key, secret3)
  key = xor(key, secret4)
  c = bytes.fromhex(ENCRYPTED_FLAG)
  print(xor(c, key).decode().strip())

def exercise_A():
  root = Tag("html", [
    Tag("head", []),
    Tag("body", [
      Tag("h1", []),
      Tag("div", [
        Tag("p", []),
        Tag("p", []),
      ]),
      Tag("div", [
        Tag("p", []),
        Tag("p", []),
        Tag("p", [], ENCRYPTED_SECRET1),
      ]),
      Tag("div", [
        Tag("p", []),
        Tag("p", []),
      ]),
    ])
  ])

  return root

def exercise_B():
  root = Tag("html", [
    Tag("head", []),
    Tag("body", [
      Tag("h1", []),
      Tag("div", [
        Tag("p", []),
        Tag("p", [], ENCRYPTED_SECRET2),
      ]),
      Tag("div", [
        Tag("p", []),
        Tag("p", []),
        Tag("p", []),
      ]),
      Tag("div", [
        start := Tag("p", []),
        Tag("p", []),
      ]),
    ])
  ])

  return start

def exercise_C():
  root = Tag("html", [
    Tag("head", [
      Tag("title", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("link", []),
      Tag("link", []),
      Tag("script", []),
      Tag("script", []),
    ]),
    Tag("body", [
      Tag("div", [
        Tag("div", [
          Tag("header", [
            Tag("div", [
              Tag("p", [
                Tag("b", []),
                Tag("i", []),
                start := Tag("span", []),
              ]),
              Tag("div", [
                Tag("img", []),
                Tag("span", []),
              ])
            ]),
          ]),
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("p", []),
              Tag("p", []),
              Tag("p", [
                Tag("b", []),
                Tag("i", []),
                Tag("span", []),
              ]),
              Tag("p", [
                Tag("b", []),
                Tag("i", []),
                Tag("span", []),
              ]),
            ]),
          ]),
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("ul", [
                Tag("li", []),
                Tag("li", [], ENCRYPTED_SECRET3),
              ]),
            ]),
          ]),
        ]),
        Tag("footer", [
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("p", []),
            ]),
          ]),
        ]),
      ]),
    ]),
    Tag("script", []),
  ])

  return start

def exercise_D():
  root = Tag("html", [
    Tag("head", [
      Tag("title", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("meta", []),
      Tag("link", []),
      Tag("link", []),
      Tag("script", []),
      Tag("script", [], ENCRYPTED_SECRET4),
    ]),
    Tag("body", [
      Tag("div", [
        Tag("div", [
          Tag("header", [
            Tag("div", [
              Tag("p", [
                Tag("b", []),
                Tag("i", []),
                Tag("span", []),
              ]),
              Tag("div", [
                Tag("img", []),
                Tag("span", []),
              ])
            ]),
          ]),
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("p", []),
              Tag("p", []),
              Tag("p", [
                Tag("b", []),
                Tag("i", []),
                Tag("span", []),
              ]),
              Tag("p", [
                Tag("b", []),
                start := Tag("i", []),
                Tag("span", []),
              ]),
            ]),
          ]),
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("ul", [
                Tag("li", []),
                Tag("li", []),
              ]),
            ]),
          ]),
        ]),
        Tag("footer", [
          Tag("div", [
            Tag("div", [
              Tag("p", []),
              Tag("p", []),
            ]),
          ]),
        ]),
      ]),
    ]),
    Tag("script", []),
  ])

  return start