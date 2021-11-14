myfile = open('cheat_sheet.txt')
print(type(myfile))
# <class '_io.TextIOWrapper'>

my_file_read = myfile.read()
print(type(my_file_read))
# <class 'str'>

print(my_file_read)
# content of the file
