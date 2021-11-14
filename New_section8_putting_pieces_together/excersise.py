# Version 1 working ok
# user_inputs = ""
# while True:
#     user_input = input("Say Something : ")
#     if user_input == '\\end':
#         break
#     else:
#         user_input = user_input.strip().capitalize() + ('?' if user_input.startswith("how") else '.')
#
#         user_inputs = user_inputs + user_input
#         continue
#
# print(user_inputs)

# Version 2

question_indicators = ("How", "What", "Why")


def create_sentence(phrase):
    capitalized = phrase.capitalize()
    append_str = ''
    if capitalized.startswith(question_indicators):
        append_str = '? '
    else:
        append_str = '. '

    return f"{capitalized}{append_str}"


user_inputs = ""
while True:
    user_input = input("Say Something : ")
    if user_input == '\\end':
        break
    else:
        user_inputs = user_inputs + create_sentence(user_input)
        continue

print(user_inputs)
