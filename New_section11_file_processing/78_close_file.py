myfile = open('78_close_file.py')
my_file_read = myfile.read()
# once processing on the file is done we should close the file
myfile.close()

print(my_file_read)

# after close if we call read it will give error IO operation on closed file
