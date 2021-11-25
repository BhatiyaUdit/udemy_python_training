# BULK renaming of the files


import glob
import os

file_names = glob.glob('./files9/file*.txt')

for file_name in file_names:
    print(file_name)
    file_name = str(file_name)
    first_part = file_name[:-5]
    x = file_name[-5:]
    print(f"{first_part}-{x}")
    os.rename(file_name, f"{first_part}-{x}")

