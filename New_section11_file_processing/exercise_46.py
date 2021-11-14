# =funtion to get single string character and file path and get the number of
# occurence of that character in the file

def get_occurences(character , file_path):
    with open(file_path) as my_file:
        content = my_file.read()
        count = content.count(character)
        return count

print(get_occurences('e','cheat.txt'))
