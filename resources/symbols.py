import json


def _get_symbol_pack(path="./resources/symbols.json"):
    with open(path, "r") as f:
        return json.load(f)


def _get_frequencies(path="./resources/letter_frequencies.json"):
    with open(path, "r") as f:
        return json.load(f)


alphabets = _get_symbol_pack()
symbol_frequency = _get_frequencies()


def _get_vigenere_alphabet():
    alpha = set("".join(alphabets.values()))
    alpha |= set("".join(chars.upper() for chars in alphabets.values()))
    return "".join(sorted(list(alpha)))


vigenere_alphabet = _get_vigenere_alphabet()

if __name__ == "__main__":
    print(alphabets)
    print(symbol_frequency)
    print(vigenere_alphabet)
