# waf to return middle item of odd numbered list
# add scenario of even length list

def foo(lst):
    if lst and len(lst) % 2 == 1:
        middle = (len(lst)) / 2
        return lst[int(middle)]
    else:
        return "Bad List"


print(foo([5, 8, 9,10]))
