# information about the number in the dictionary

# {'sign' : 'positive', parity : 'even'}

def foo(number):
    result = {'sign': 'positive' if number > 0 else 'negative' if number < 0 else 'zero'
        , 'parity': 'non-integer' if type(number) != int else 'even' if number % 2 == 0 else 'odd'}

    return result


print(foo(3.14))


def foo2(number):
    return dict(sign="positive" if number > 0 else
    ("negative" if number < 0 else "zero"),
                parity="odd" if number % 2 == 1 else
                ("even" if number % 2 == 0 else "non integer"))
