import json


def _get_symbol_pack(path="./resources/symbols.json"):
    with open(path, "r") as f:
        return json.load(f)


def _get_frequencies(path="./resources/letter_frequencies.json"):
    with open(path, "r") as f:
        return json.load(f)


supported_symbols = _get_symbol_pack()
symbol_frequency = _get_frequencies()

if __name__ == "__main__":
    print(_get_symbol_pack("../resources/symbols.json"))
    print(_get_frequencies("../resources/letter_frequencies.json"))
