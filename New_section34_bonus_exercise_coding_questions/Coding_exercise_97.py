# read file all lines
# extract numbers
# find mean

import re
import glob

files = glob.glob('./files3/*.txt')
print(files)

nums = []
for file_name in files:
    with open(file_name) as file:
        lines = file.readlines()
        regex = re.compile("[0-9]+\.*[0-9]*")
        print(lines)
        for line in lines:
            number_pos = regex.search(line)
            if number_pos:
                number = number_pos.group()
                nums.append(float(number))



print(sum(nums)/len(nums))




# import glob
# import re
#
# text_files = glob.glob("*.txt")
# lists =[]
# for text_file in text_files:
#     with open(text_file) as file:
#         lists.append(file.readlines())
#
# all_lines = sum(lists, [])
#
# matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]
#
# numbers = [float(match.group(0)) for match in matches if match]
# print(sum(numbers)/len(numbers))