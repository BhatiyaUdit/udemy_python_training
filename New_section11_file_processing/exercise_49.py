# append the text of bear1.txt to bear2.text

with open('bear1.txt') as bear1:
    bear_content = bear1.read()


with open('bear2.txt', 'a') as first_f:
    first_f.write(bear_content)