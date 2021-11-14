
# use with context manager to read the files

with open('cheat_sheet.txt') as txtFile:
    content = txtFile.read()


print(content)

# advantage no need to write close , more structured code
