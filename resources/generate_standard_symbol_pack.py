from string import ascii_lowercase, ascii_uppercase, punctuation
import json


def generate():
    rus_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_uppercase = rus_lowercase.upper()

    symbols = {
        "eng_lowercase": ascii_lowercase,
        "eng_uppercase": ascii_uppercase,
        "rus_lowercase": rus_lowercase,
        "rus_uppercase": rus_uppercase,
        "other": " " + punctuation
    }

    with open("symbols.json", "w") as f:
        json.dump(symbols, f)


if __name__ == "__main__":
    generate()
