import json

data = json.load(open("../data/data.json"))


def get_definition(word):
    return data[word]


user_ip = input("Enter word : ")

print(get_definition(user_ip))
