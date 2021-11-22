# create 9 empty text file with name day1.txt, day2.txt....

# only create when file is not present


for i in range(1, 10):
    try:
        with open(f'./files2/day{i}.txt', 'x') as file:
            file.close()
    except FileExistsError as e:
        pass



# can use a to assume to append to a file instead of using x