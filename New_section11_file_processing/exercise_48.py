# create a file with name first.txt and write first 90 characters of bear.txt

with open('bear.txt') as bear:
    bear_content = bear.read()
    first_90 = bear_content[:91]

with open('first.txt', 'w') as first_f:
    first_f.write(first_90)


with open('first.txt') as c:
    cp = c.read()
    print(len(cp))