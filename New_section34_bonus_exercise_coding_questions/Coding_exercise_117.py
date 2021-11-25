# Similarity between texts


import difflib


def foo(string1, string2):
    return difflib.SequenceMatcher(None, string1, string2).ratio()


print(foo("tell me the time", "what time is it"))
