from googletrans import Translator


def translate(text):
    dest = "hi"
    translator = Translator()
    return translator.translate(text=text, dest=dest).text
