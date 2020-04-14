from string import ascii_lowercase, ascii_uppercase, punctuation
import json


def generate():

    cyrillic_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    cyrillic_uppercase = cyrillic_lowercase.upper()

    symbols = {
        "latin_lowercase": ascii_lowercase,
        "latin_uppercase": ascii_uppercase,
        "cyrillic_lowercase": cyrillic_lowercase,
        "cyrillic_uppercase": cyrillic_uppercase,
        "other": " " + punctuation
    }

    with open("symbols.json", "w") as f:
        json.dump(symbols, f)


if __name__ == "__main__":
    generate()
