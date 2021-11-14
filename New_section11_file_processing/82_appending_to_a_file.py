# if file exists content is appended
# if file does not exists then file will be created

with open('cheat1.txt', 'a') as newFile:
    newFile.write("\nHEllo New file")
    newFile.write(" after first line")
    newFile.write("\n new line")

#    newFile.read()
# io.UnsupportedOperation: not readable
# cant read when mode is 'a'

# reading while appending
# seek is used to reset the cursor

with open('cheat1.txt', 'a+') as newFile:
    newFile.write("\nHEllo New file")
    newFile.write(" after first line")
    newFile.write("\n new line")
    newFile.seek(0)
    content = newFile.read()
    print(content)
