import cv2

imsss = cv2.imread('1_smallgray.png', 0)

print(imsss)
print(type(imsss))

# filtering data from numpy array
# [[187 158 104 121 143]
#  [198 125 255 255 147]
#  [209 134 255  97 182]]

# from the above array we need to extract
# [
#  [104 121]
#  [255 255]
# ]
# just like index access in list we can do same here (end index is not inclusive)

# slicing ~~~~~~~~~~~~~~~~~~~~
print(imsss[0:2, 2:4])

# shape of array
print(imsss.shape)


# indexing ~~~~~~~~~~~~~~~~~
# getting only one element
print(imsss[2, 3])  # 97
print(imsss[2][2]) # 255

# both syntax are fine to access the elements in multi-dimensional array



# iteration through numpy array ~~~~~~~~~~~~~~

# printing rows
for i in imsss:
    print(i)

# printing columns

for i in imsss.T:
    print(i)

# for printing all the values in a linear fashion
# row by row then column by column
for i in imsss.flat:
    print(i)