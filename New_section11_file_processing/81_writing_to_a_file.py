
# if file exists content is overwritten
# if file does not exists then file will be created

with open('cheat.txt','w') as newFile:
    newFile.write("HEllo New file")
    newFile.write(" after first line")
    newFile.write("\n new line")


