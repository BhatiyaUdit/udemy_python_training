# print in format

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, val in phone_numbers.items():
    print(key + ":" + " " + val)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for num in phone_numbers.values():
    print(num.replace('+','00'))
