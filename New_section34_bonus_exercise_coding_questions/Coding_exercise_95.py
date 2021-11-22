# create 9 empty text file with name day1.txt, day2.txt....


for i in range(1, 10):
    with open(f'./files/day{i}.txt', 'w') as file:
        file.close()


# for number in range(1, 9+1):
#     open("day{}.txt".format(number), "w").close()