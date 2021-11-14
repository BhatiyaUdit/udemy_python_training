import json
from difflib import SequenceMatcher

data = {"rain": "rain"}


def get_definition(word):
    word = word.lower()
    ratoo = SequenceMatcher(None, word, "rain").ratio()
    print(ratoo)
    if word in data:
        return data[word]
    else:
        return "Word is not present"


user_ip = input("Enter word : ")

print(get_definition(user_ip))
