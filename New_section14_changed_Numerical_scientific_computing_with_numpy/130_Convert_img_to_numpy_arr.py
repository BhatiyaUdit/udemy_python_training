import cv2

print(cv2.version)

# second argument -> 0 = grayScale ~~~~ 1= BGR this will return a 3-d array
# 3d array will have values array for B layer , G layer, R layer in separate 2d array inside the parent array

imsss = cv2.imread('1_smallgray.png', 0)

print(imsss)
print(type(imsss))
imsss[0] = 255
print(imsss)
# create image from numpy array

cv2.imwrite('2_new.png', imsss)