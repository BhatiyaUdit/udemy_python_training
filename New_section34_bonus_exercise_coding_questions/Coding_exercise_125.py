# Object id
# print out id of the object


def foo(obj:int):
    print(obj.__sizeof__())
    return id(obj)


print(foo(3))
