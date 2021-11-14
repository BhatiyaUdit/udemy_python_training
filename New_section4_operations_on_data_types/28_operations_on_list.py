list_of_marks = [30.5, 45, 59.5]
print(list_of_marks)

# append element at the end
list_of_marks.append(55)

print("List after element is added", list_of_marks)

# remove all from list
list_of_marks.clear()

print("List after clear", list_of_marks)

# get index of a value

list_of_marks = [30.5, 45, 59.5]
index_of_45 = list_of_marks.index(45)
print(index_of_45)

# get index of a value with start as 2

list_of_marks = [30.5, 45, 59.5, 45, 60]
index_of_45 = list_of_marks.index(45, 2)
print(index_of_45)


# value error when element not found
sample = list_of_marks.index(75)

