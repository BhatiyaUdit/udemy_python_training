# create 50 empty folders
# 1/ , 2/

# and all folders should have 7 empty sub-folders 'monday, tuesday...'

import os


days = ['mon', 'tue', 'wed', 'thu', 'fri']

for i in range(1, 51):
    os.mkdir(f'paths2/{i}')
    for day in days:
        os.mkdir(f'paths2/{i}/{day}')

