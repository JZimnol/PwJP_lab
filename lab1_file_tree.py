import os
from pathlib import Path

FILE_PATH = "ENTER_YOUR_FILE_PATH"

for root, subdirs, files in os.walk(FILE_PATH):
    for file in files:
        print(os.path.join(root, file))

print("-----------------------------------------")


def print_tree(input_path):
    p = Path(input_path)
    for path in p.iterdir():
        if not path.is_dir():
            print(path)
    for path in p.iterdir():
        if path.is_dir():
            print_tree(path)


print_tree(FILE_PATH)

print("-----------------------------------------")

p = Path(FILE_PATH)
for file in p.glob('*'):
    print(file)
