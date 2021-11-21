# complete the code based on comments


# Function gets a list, converts it to tuple and returns the tuple
def list_to_tuple(lst):
    return tuple(lst)


# Function gets any Python class object (e.g. str, int, float, etc)
# and returns the object name as string (i.e. 'str', 'int', 'float')
def object_to_string(object):
    print(object.__name__)
    print(type(object))
    x = type(object)
    print(x, type(x))
    return str(x)


print(list_to_tuple([1, 112]))
print(object_to_string(float))
