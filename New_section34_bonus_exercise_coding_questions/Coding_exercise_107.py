# REad dict from a file and load a spedific value from key
import json

with open('./files6/file2.txt') as read_dict:
    dict_data:dict = json.load(read_dict)
    read_dict.close()

print(dict_data)

print(dict_data.get('metals').get('steel').get('density'))
