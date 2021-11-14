# create a function that takes a list with strings numbers and returns sum of those numbers
# replace string with 0

def return_number_list(data):
    temp_list = [float(value) if type(value) == str else value for value in data]
    return sum(temp_list)


print(return_number_list(['1', '2', '3', 4]))
