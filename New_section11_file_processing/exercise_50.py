# append the existing content 2 more times

with open('data.txt','a+') as data:
    data.seek(0)
    content = data.read()
    data.write(content)
    data.write(content)

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)