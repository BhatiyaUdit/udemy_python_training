# CHATBOT Version 2.0

# when talk function called with vocab
# then should return proper response

# v2 when response not found then should return 'I don't understand that!'
# v3 it should know the query what time is it ?
# v4 somewhat intelligent bot with word ratio comparison
import datetime
import difflib

vocabulary = {
    "hello": "Hi there!",
    "what's your name": "My name is Roboto!",
    "what is your name": "My name is Roboto!",
    "bye": "Goodbye!",
    "what time is it": datetime.datetime.now().strftime("%H:%M")
}


def talk(query, vocabulary):
    ratio = 0
    key_ = None
    for key in vocabulary.keys():
        x = difflib.SequenceMatcher(a=query, b=key).ratio()
        if x > ratio:
            ratio = x
            key_ = key

    print(ratio, key_)

    if key_ in vocabulary:
        return vocabulary[key_]
    else:
        return "I don't understand that!"


print(talk("what", vocabulary))


def foo(query, vocabulary):
    new_vocabulary = {key: [value, difflib.SequenceMatcher(None, query, key).ratio()]
                      for (key, value) in vocabulary.items()}
    print("NEw", new_vocabulary)
    print(max(new_vocabulary, key=lambda k: new_vocabulary[k][1]))
    return new_vocabulary[max(new_vocabulary, key=lambda k: new_vocabulary[k][1])][0]


print(foo("what", vocabulary))
