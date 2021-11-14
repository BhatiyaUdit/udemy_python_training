# loop over a list
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)


# 31 loop over and print if value is greater than 50

colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color > 50 :
        print(color)

print()
#32 loop over and print if the val is int
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color) == int:
        print(color)



print()
#33 loop over and print if the val is int and greater than 50
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if type(color) == int and color > 50:
        print(color)
