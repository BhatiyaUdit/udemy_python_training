# CHATBOT Version 2.0

# when talk function called with vocab
# then should return proper response

# v2 when response not found then should return 'I don't understand that!'


vocabulary = {
    "hello": "Hi there!",
    "what's your name": "My name is Roboto!",
    "what is your name": "My name is Roboto!",
    "bye": "Goodbye!"
}


def talk(query, vocabulary):
    return vocabulary.get(query) if vocabulary.get(query) else "I don't understand that!"


print(talk("what time is it", vocabulary))
