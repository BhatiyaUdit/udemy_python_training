# if want condition inside the loop we can put if and else in list comprehension

temps = [221, 234, 320, -888, 421]

# SYNTAX needs to be changed and for loop will come later after if/else

new_temps_2 = [temp / 10 if temp > 0 else 0 for temp in temps]
print(new_temps_2)

# output
# [22.1, 23.4, 32.0, 0, 42.1]
