# CHATBOT Version 2.0

# when talk function called with vocab
# then should return proper response

# v2 when response not found then should return 'I don't understand that!'
# v3 it should know the query what time is it ?
import datetime
import time

vocabulary = {
    "hello": "Hi there!",
    "what's your name": "My name is Roboto!",
    "what is your name": "My name is Roboto!",
    "bye": "Goodbye!"
}


def talk(query, vocabulary):
    if 'time' in query and 'what' in query:
        return f"{datetime.datetime.now():%H:%M}"
    return vocabulary.get(query) if vocabulary.get(query) else "I don't understand that!"


print(talk("what time is it", vocabulary))



### INSTRUCTOR

import datetime

vocabulary = {
    "hello" : "Hi there!",
    "what's your name" : "My name is Roboto!",
    "what is your name" : "My name is Roboto!",
    "bye" : "Goodbye!",
    "what time is it" : datetime.datetime.now().strftime("%H:%M")
}

def foo(query, vocabulary):
    if query in vocabulary:
        return vocabulary[query]
    else:
        return "I don't understand that!"
