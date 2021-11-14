dict_1 = {
    "hello": 1,
    "world": 2,
    "!!": 3
}

print("Items")
for item in dict_1.items():
    print(item, type(item))

print()
print("Keys")
for item in dict_1.keys():
    print(item)

print()
print("Values")
for item in dict_1.values():
    print(item)

