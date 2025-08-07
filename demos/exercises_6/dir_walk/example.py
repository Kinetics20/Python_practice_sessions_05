import weirdfs

with open("fscontents.bin", "rb") as f:
  fs_content = f.read()
fs = weirdfs.ReadOnlyWeirdFileSystem(fs_content)

# Checking if something is a file or a directory.
print(fs.is_file("/i/dont/exist"))   # False (doesn't exist)
print(fs.is_file("/"))               # False (it's a dir)
print(fs.is_dir("/"))                # True
print(fs.is_file("/test"))           # False (it's a dir)
print(fs.is_dir("/test"))            # True
print(fs.is_file("/test/test"))      # False (it's a dir)
print(fs.is_dir("/test/test"))       # True
print(fs.is_file("/test/test/test")) # True
print(fs.is_dir("/test/test/test"))  # False (it's a file)

# Opening and reading an existing file.
print(fs.open_file("/test/test/test", "rb").read())
print(fs.open_file("/test/test/test", "r").read())

# Changing the directory (absolute path).
print(fs.chdir("/test"))
print(fs.open_file("test/test", "rb").read())
print(fs.open_file("test/test", "r").read())

# Changing the directory (relative path).
print(fs.chdir("test"))
print(fs.open_file("test", "rb").read())
print(fs.open_file("test", "r").read())

# Changing the directory (absolute path with subpaths).
print(fs.chdir("/test/test"))
print(fs.open_file("test", "rb").read())
print(fs.open_file("test", "r").read())

# Changing the directory back to FS root.
print(fs.chdir("/"))
