# Build try and except

# print sum of x and y  in try block
# print sum of integer version of x and y in except block


x = 1
y = '2'

try:
    print(x + y)
except TypeError as te:
    print(int(x) + int(y))
