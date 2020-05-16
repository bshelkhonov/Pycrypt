import string

alphabets = {
    "eng": string.ascii_lowercase,
    "rus": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "other": " " + string.punctuation
}


def _get_vigenere_alphabet():
    alpha = set("".join(alphabets.values()))
    alpha |= set("".join(chars.upper() for chars in alphabets.values()))
    return "".join(sorted(list(alpha)))


vigenere_alphabet = _get_vigenere_alphabet()
