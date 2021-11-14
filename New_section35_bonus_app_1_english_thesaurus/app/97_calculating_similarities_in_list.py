import json
from difflib import get_close_matches
from datetime import datetime

data =json.load(open("../data/data.json"))


def get_definition(word):
    word = word.lower()
    matched_val = get_close_matches(word, data.keys(),1)
    print(matched_val)
    if len(matched_val) > 0:
        print("inside true")
    else:
        print("inside false")

    if word in data:
        return data[word]
    else:
        return "Word is not present"


user_ip = input("Enter word : ")
print(datetime.now())
print(get_definition(user_ip))
print(datetime.now())