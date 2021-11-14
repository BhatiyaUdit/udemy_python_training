students = {
    "udit": 75,
    "abcd": 65,
    "efgh": 85
}

# if we want sum of values

values = students.values()

print(values)
# dict_values([75, 65, 85])
print(type(values))
# <class 'dict_values'>
# Not a list but behaves like a list

sum_of_values = sum(values)
print(sum_of_values)

print(students.keys(), type(students.keys()))
# dict_keys(['udit', 'abcd', 'efgh']) <class 'dict_keys'>
