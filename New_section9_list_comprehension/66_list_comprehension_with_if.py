# if want condition inside the loop we can put if in list comprehension

temps = [221, 234, 320, -888, 421]

new_temps_2 = [temp / 10 for temp in temps if temp > 0]
print(new_temps_2)

# output
# [22.1, 23.4, 32.0, 42.1]
