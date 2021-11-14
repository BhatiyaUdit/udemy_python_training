# Numpy is the base library for the libraries like
# PANDAS And OpenCV (image processing)

# we can create numpy arrays based on the lists and then use them for processing


import numpy

n = numpy.arange(27)
# creates an ndimensional array object
print(n)
print(type(n))

n = n.reshape(9, 3)
print(n)

n = n.reshape(3, 3, 3)
print(n)

# we can also create n-d array with exisiting list
m = numpy.asarray([[1,2,3], [] , [2222 ,3333]], dtype=object)
print(m)
