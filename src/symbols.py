import json


def _get_symbol_pack(path="./resources/symbols.json"):
    with open(path, "r") as f:
        return json.load(f)


supported_symbols = _get_symbol_pack()

if __name__ == "__main__":
    print(_get_symbol_pack("../resources/symbols.json"))
