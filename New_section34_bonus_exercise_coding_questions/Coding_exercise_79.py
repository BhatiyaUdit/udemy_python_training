# print the mean of list items at a step of 2
# sum every second item and calculate mean

# need to print the mean only

numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6, 77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 8, 8, 9, 8, 8, 0, 9, 0, 9, 8, 9,
           8, 8, 8, 9, 9, 9, 9, 0, 1, 3, 5, 6, 7, 8, 7, 7, 7, 8, 7, 7, 5, 4, 5, 6, 5, 56, 4, 3, 4, 5, 6, 6, 7, 8, 8, 9]

new_list = numbers[::2]

print(new_list, sum(new_list), sum(new_list)/len(new_list))