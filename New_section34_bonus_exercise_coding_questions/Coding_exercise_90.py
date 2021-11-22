# CHATBOT Version 1.0

# when talk function called with vocab
# then should return proper response


vocabulary = {
    "hello": "Hi there!",
    "what's your name": "My name is Roboto!",
    "what is your name": "My name is Roboto!",
    "bye": "Goodbye!"
}


def talk(query, vocabulary):
    return vocabulary.get(query)


print(talk("what time is it", vocabulary))
