from string import ascii_letters, ascii_lowercase, ascii_uppercase
import unicodedata

cyrillic_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cyrillic_uppercase = cyrillic_lowercase.upper()
cyrillic_letters = cyrillic_lowercase + cyrillic_uppercase

punctuation = ""


def _find_all_punctuation():
    global punctuation

    for index in range(140000):
        if unicodedata.category(chr(index))[0] == "P":
            punctuation += chr(index)


_find_all_punctuation()
