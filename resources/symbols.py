import json


def _get_symbol_pack(path="./resources/symbols.json"):
    with open(path, "r") as f:
        return json.load(f)


def _get_frequencies(path="./resources/letter_frequencies.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return dict()


def _get_most_common_words(path="./resources/most_common_words.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
        for pack in data:
            data[pack] = set(data[pack])
        return data

    except json.decoder.JSONDecodeError:
        return dict()


alphabets = _get_symbol_pack()
symbol_frequency = _get_frequencies()
most_common_words = _get_most_common_words()


def _get_vigenere_alphabet():
    alpha = set("".join(alphabets.values()))
    alpha |= set("".join(chars.upper() for chars in alphabets.values()))
    return "".join(sorted(list(alpha)))


vigenere_alphabet = _get_vigenere_alphabet()

if __name__ == "__main__":
    print(alphabets)
    print(symbol_frequency)
    print(vigenere_alphabet)
