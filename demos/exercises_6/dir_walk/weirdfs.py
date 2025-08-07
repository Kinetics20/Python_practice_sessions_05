from io import BytesIO, StringIO
import hashlib

TYPE_FILE = 0
TYPE_DIR = 1

class ReadOnlyWeirdFileSystem:
  def __init__(self, fs_contents):
    self.current_dir = []
    self.fs_contents = fs_contents

  def _split_path(self, path):
    return [p for p in path.split('/') if p]

  def _join_path(self, *paths):
    return '/'.join(paths)

  def _path_to_canon_abs(self, path):
    # This function does not check if the path exists.

    if path.startswith('/'):
      new_dir = []
    else:
      new_dir = self.current_dir[:]

    path = self._split_path(path)

    for p in path:
      if p == '..':
        try:
          new_dir.pop()
        except IndexError:
          pass  # Not an error.
      elif p == '.':
        continue
      else:
        new_dir.append(p)

    return '/' + self._join_path(*new_dir)

  def _path_hash256(self, path):
    canon_path = self._path_to_canon_abs(path)
    return hashlib.sha256(canon_path.encode()).digest()

  def _path_hash512(self, path):
    canon_path = self._path_to_canon_abs(path)
    return hashlib.sha512(canon_path.encode()).digest()

  def _get_content(self, path):
    h = self._path_hash256(path)
    off = self.fs_contents.find(h)
    if off == -1:
      return None

    off += 32
    c = self.fs_contents[off:off+64]
    k = self._path_hash512(path)
    return bytes([a^b for a, b in zip(c, k)])

  def is_file(self, path):
    c = self._get_content(path)
    if c is None:
      return False

    return c[0] == TYPE_FILE

  def is_dir(self, path):
    c = self._get_content(path)
    if c is None:
      return False

    return c[0] == TYPE_DIR

  def chdir(self, path):
    new_path = self._path_to_canon_abs(path)

    if self.is_file(new_path):
      raise NotADirectoryError(f"File {new_path} is, well, a file")

    if not self.is_dir(new_path):
      raise FileNotFoundError(f"Directory {new_path} not found")

    self.current_dir = self._split_path(new_path)
    return new_path

  def open_file(self, path, mode):
    if self.is_dir(path):
      raise IsADirectoryError(f"Directory {path} is, well, a directory")

    if not self.is_file(path):
      raise FileNotFoundError(f"File {path} not found")

    if mode not in ["rb", "r"]:
      raise ValueError(
        f"Invalid mode: {mode} - only 'rb' and 'r' are supported"
      )

    content = self._get_content(path)
    if content is None:
      assert False, f"Should never happen: {path}"

    sz = content[1]
    assert sz <= 62, f"FS content is corrupted: {path}"
    data = content[2:2+sz]

    if mode == "rb":
      return BytesIO(data)
    elif mode == "r":
      return StringIO(data.decode())

    assert False, f"Should never happen: {path}, {mode}"


