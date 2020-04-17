from src.caesar import CaesarCypher
from src.vigenere import VigenereCypher
from src.vernam import VernamCypher
import argparse
import sys

cyphers = {
    "caesar": CaesarCypher,
    "vigenere": VigenereCypher,
    "vernam": VernamCypher
}


is_integer_key = {
    "caesar": True,
    "vigenere": False,
    "vernam": False
}


def encode(text, key, cypher):
    if is_integer_key[cypher]:
        return getattr(cyphers[cypher], "encode")(text, int(key))
    return getattr(cyphers[cypher], "encode")(text, key)


def decode(text, key, cypher):
    if is_integer_key[cypher]:
        return getattr(cyphers[cypher], "decode")(text, int(key))
    return getattr(cyphers[cypher], "decode")(text, key)


functions = {
    "encode": encode,
    "decode": decode,
    "hack": CaesarCypher.hack,
}


def read_file(file):
    return "".join(file.readlines())


def make_parser():
    parser = argparse.ArgumentParser(description="Crypt")
    parser.add_argument("mod", help="working mod - encoding")
    parser.add_argument("--input_file", help="file with text to work")
    parser.add_argument("--output_file", help="file to write result")
    parser.add_argument("--cypher", help="cypher algorithm")
    parser.add_argument("--key", help="key for cypher")
    return parser


def main():
    args = make_parser().parse_args()

    if args.input_file is None:
        text = read_file(sys.stdin)
    else:
        with open(args.input_file, "r") as f:
            text = read_file(f)

    processed_text = ''
    if args.key is not None:
        processed_text = functions[args.mod](text, args.key, args.cypher)

    if args.output_file is None:
        print(processed_text)
    else:
        with open(args.output_file, "w") as f:
            f.write(processed_text)


if __name__ == "__main__":
    main()
