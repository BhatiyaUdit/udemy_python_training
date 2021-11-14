def myFunc(list_):
    # function should be able to check btw list and dictionary
    if type(list_) == dict:
        mean_value = sum(list_.values()) / len(list_)
    else:
        mean_value = sum(list_) / len(list_)
    
    return mean_value


student_grades = {
    "I": 45,
    "me": 55,
    "mine": 56
}

print(myFunc(student_grades))
