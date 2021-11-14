# print first 90 characters from a file
with open('bear.txt') as myFile:
    content = myFile.read()
    print(content[:91])