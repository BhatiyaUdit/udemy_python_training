# Print the first item of the list if the item is integer

elements = [
    [1, 4, 6, 7],
    [4, 5, 6],
    [6, 7, 8],
    [],
    ["nodata", "nodata"],
    [1, 3]
]


for l in elements:
    if l and len(l)>0 and type(l[0]) == int:
        print(l[0])

for lst in elements:
    if lst and isinstance(lst[0], int):
        print(lst[0])