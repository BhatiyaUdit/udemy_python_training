# to print out attributes available on the type
# attributes can be property or method

print(dir(list))

print(dir(int))

print(dir(float))

print(help(str.upper))

# we can also print the details of built in methods like print

print(dir(__builtins__))

print(help(dir))

print(dir())

# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']