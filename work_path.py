from pathlib import Path

path = Path("ecommerce/__init__.py")

print(path)

path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_name("file.txt")
print(path.absolute())
print(path)

path = path.with_suffix(".txt")
print(path)

