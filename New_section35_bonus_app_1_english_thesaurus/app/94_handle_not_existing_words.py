import json

data = json.load(open("../data/data.json"))


def get_definition(word):
    if word in data:
        return data[word]
    else:
        return "Word is not present"


user_ip = input("Enter word : ")

print(get_definition(user_ip))
