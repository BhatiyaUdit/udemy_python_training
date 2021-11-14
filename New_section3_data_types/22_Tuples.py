# tuples are like lists but are immutable
# cant add/remove elements from tuples

var = (1, 2, 3)
print(type(var))
# <class 'tuple'>

print(dir(tuple))

print(help(tuple.__add__))

# can be used to concat another tuple (no direct add/remove elements methods)
var2 = var.__add__(var)
print(var2)
