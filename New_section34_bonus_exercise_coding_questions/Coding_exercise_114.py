# String formatting

names = {"firstname": "Andy", "lastname": "Smith"}
firstname = names.get('firstname')
lastname = names.get('lastname')
print("Welcome {firstname} {lastname} to our shop!".format(**locals()))

print("Welcome {firstname} {lastname} to our shop!".format(**names))
