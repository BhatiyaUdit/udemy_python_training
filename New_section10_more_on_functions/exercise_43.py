# pass such args as the output becomes 9

def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=6, b=3))