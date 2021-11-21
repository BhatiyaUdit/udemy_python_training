# print all the numbers from 0 to 10 with increment of 0.1


for x in range(0, 101, 1):
    print(x / 10)


for i in (x / 10 for x in range(0, 101)):
    print(i)