# Use Case , to save server space sometimes it is done like data is stored as integers instead of decimals
# using integers can save space as it will consume less number of bytes
# and we can divide the values later while consuming only


# Option 1 for loop
temps = [221, 234, 320, 421]

new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# option 2 list comprehension
# TODO : see more about its syntax
new_temps_2 = [temp / 10 for temp in temps]
print(new_temps_2)
