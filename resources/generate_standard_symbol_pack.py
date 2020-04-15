from string import ascii_lowercase, ascii_uppercase, punctuation
import json


def generate():
    rus_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    symbols = {
        "eng": ascii_lowercase,
        "rus": rus_lowercase,
        "other": " " + punctuation
    }

    with open("symbols.json", "w") as f:
        json.dump(symbols, f)


if __name__ == "__main__":
    generate()
