import cv2
import numpy

imsss = cv2.imread('1_smallgray.png', 0)
print(imsss)

# stacking another array to existing arr
# arrays must have same dimensions


# 1. horizontal stacking
# hstack method needs one argument only and we can pass a tuple containing multiple arrays

im_hstack = numpy.hstack((imsss, imsss))
print(im_hstack)

# 2. vertical stacking
# vstack method needs one argument only and we can pass a tuple containing multiple arrays

im_vstack = numpy.vstack((imsss, imsss))
print(im_vstack)

# Splitting
# Breaking up a bigger array into smaller arrays

# 1. horizontal split ( two args ) numpy array and how many smaller arrays are needed
# number of columns must be divisible by the number of arrays that needs to be created

h_split = numpy.hsplit(im_hstack, 2)
print(h_split)

# h_split is a list of numpy arrays

# 2. vertical split ( two args ) numpy array and how many smaller arrays are needed
# number of rows must be divisible by the number of arrays that needs to be created

v_split = numpy.vsplit(im_vstack, 3)
print(v_split)

# v_split is a list of numpy arrays
