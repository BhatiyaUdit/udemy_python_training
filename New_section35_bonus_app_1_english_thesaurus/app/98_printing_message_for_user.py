import json
from difflib import get_close_matches
from datetime import datetime

data = json.load(open("../data/data.json"))


def get_definition(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        matched_val = get_close_matches(word, data.keys())
        print(f"Did you mean '{matched_val[0]}' instead ? ")
    else:
        return "Word is not present"


user_ip = input("Enter word : ")
print(datetime.now())
print(get_definition(user_ip))
print(datetime.now())
