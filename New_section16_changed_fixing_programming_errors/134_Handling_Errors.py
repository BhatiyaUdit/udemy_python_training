def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Excpet"


print(divide(1, 0))
print("After expetion")
