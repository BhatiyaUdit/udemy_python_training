# print out the name of the file with smallest file size

import os
import glob
from pathlib import Path

files = glob.glob('*.py')
size = []
for file in files:
    # # print(file, type(file))
    # x = os.fspath(file)
    # p = Path(x)
    # print(p,p.stat().st_size)
    print(os.stat(file).st_size)
    size.append({'name': file, 'file_size': os.stat(file).st_size})

print(size)
print(min(size, key=lambda x: x['file_size'])['name'])


### instructor solution :

text_files = glob.glob("./files/*.txt")

sizes = {text_file:os.path.getsize(text_file) for text_file in text_files}
print(sizes)
print(min(sizes, key=sizes.get))
