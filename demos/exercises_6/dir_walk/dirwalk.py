import weirdfs

def load_names(path="weird-dir-name-list.txt"):
    with open(path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def find_all_files(fs, current_path, names, visited):
    for name in names:
        new_path = f"{current_path}/{name}".replace("//", "/")
        if new_path in visited:
            continue
        visited.add(new_path)

        if fs.is_dir(new_path):
            try:
                fs.chdir(new_path)
                print(f"[DIR] -> {new_path}")
                find_all_files(fs, new_path, names, visited)
                fs.chdir(current_path)
            except Exception as e:
                print(f"    [ERROR chdir] {new_path}: {e}")
        elif fs.is_file(new_path):
            try:
                with fs.open_file(new_path, "r") as f:
                    content = f.read()
                    print(f"\n[FOUND FILE] {new_path}\n{content}\n{'-'*60}")
            except Exception as e:
                print(f"    [ERROR read] {new_path}: {e}")

if __name__ == "__main__":
    with open("fscontents.bin", "rb") as f:
        fs_content = f.read()

    fs = weirdfs.ReadOnlyWeirdFileSystem(fs_content)

    names = load_names()
    print(f"Loaded {len(names)} names")
    print("=" * 60)
    find_all_files(fs, "/", names, set())
