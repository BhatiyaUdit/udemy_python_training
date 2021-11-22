# delete all text files


import os
import glob

files = glob.glob('./files4/*.txt')

for file in files:
    os.remove(file)
