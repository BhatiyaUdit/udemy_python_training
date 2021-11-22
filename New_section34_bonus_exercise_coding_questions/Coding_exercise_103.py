# delete all text files
# that have xxx or 'XXX' in the content


import os
import glob

files = glob.glob('./files5/*.txt')

for file in files:
    with open(file) as file_:
        data = file_.read()
        data = data.lower()
        file_.close()
    if 'xxx' in data:
        os.remove(file)
