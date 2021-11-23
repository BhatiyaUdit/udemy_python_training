# REad dict from a file and multiply all values against keys by 2
import json

with open('./files7/file2.txt') as read_dict:
    dict_data = json.load(read_dict)
    read_dict.close()

print(dict_data)

new_dict = {key: value * 2 for key, value in dict_data.items()}

print(new_dict)


def multiplier(num):
    return num * 2


for key, value in dict_data.items():
    val = lambda value: value * 2
    print(val(value))
