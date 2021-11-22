# read file all lines
# extract numbers
# find mean

# write mean to new file
import re
import glob

files = glob.glob('./files3/file*.txt')
# print(files)

nums = []
for file_name in files:
    with open(file_name) as file:
        lines = file.readlines()
        regex = re.compile("[0-9]+\.*[0-9]*")
        # print(lines)
        for line in lines:
            number_pos = regex.search(line)
            if number_pos:
                number = number_pos.group()
                nums.append(float(number))

mean = sum(nums) / len(nums)

with open('./files3/mean.txt', 'w') as file_m:
    file_m.write(str(mean))
