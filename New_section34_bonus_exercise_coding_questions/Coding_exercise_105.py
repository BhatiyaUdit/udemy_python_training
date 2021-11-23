# Add a dictionary to a existing dict present in a file
import json

with open('./files6/file2.txt') as read_dict:
    data = read_dict.read()
    dict_data = json.loads(data)
    read_dict.close()

print(dict_data)

print(dict_data['metals']['steel'])

dict_data['metals']['gold'] = {
    "conductivity": 33.5,
    "density": 0.255,
    "heat": 0.129,
    "melting point": 2171,
    "thermal expansion": 4.7,
    "yield strength": 288,
    "tensile strength": 441,
    "minimum impact energy": 22
}

str_data = json.dumps(dict_data)

with open('./files6/file2.txt', 'w') as write_dict:
    write_dict.write(str_data)
    write_dict.close()

## TRY TO USE json load and dump (refer file directly)
