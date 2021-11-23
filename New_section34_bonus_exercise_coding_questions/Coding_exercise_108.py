# WAF to return a property of a metal from a specific file
# REad dict from a file and load a spedific value from key

import json


def goo(metal, prop, filename):
    with open(filename) as read_dict:
        dict_data: dict = json.load(read_dict)
        read_dict.close()
    return dict_data.get('metals').get(metal).get(prop)


print(goo('steel', 'density', './files6/file2.txt'))
