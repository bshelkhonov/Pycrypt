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


def input_text(input_file):
    return "".join(input_file.readlines())


def output_text(text, output_file):
    output_file.write(text)


def encode(args):
    text = input_text(args.input_file)
    key = int(args.key) if is_integer_key[args.cypher] else args.key
    processed_text = cyphers[args.cypher].encode(text, key)
    output_text(processed_text, args.output_file)


def decode(args):
    text = input_text(args.input_file)
    key = int(args.key) if is_integer_key[args.cypher] else args.key
    processed_text = cyphers[args.cypher].decode(text, key)
    output_text(processed_text, args.output_file)


def hack(args):
    text = input_text(args.input_file)
    processed_text = cyphers[args.cypher].hack(text)
    output_text(processed_text, args.output_file)


def read_file(file):
    return "".join(file.readlines())


def make_parser():
    parser = argparse.ArgumentParser(description="Crypt")

    subparsers = parser.add_subparsers()

    encode_parser = subparsers.add_parser("encode", help="For command encode")
    encode_parser.set_defaults(mode="encode", func=encode)
    encode_parser.add_argument("--input_file", default=sys.stdin,
                               type=argparse.FileType("r"), help="Input file")
    encode_parser.add_argument("--output_file", default=sys.stdout,
                               type=argparse.FileType("w"), help="Output file")
    encode_parser.add_argument("--cypher",
                               choices=["caesar", "vigenere", "vernam"],
                               help="Cypher algorithm", required=True)
    encode_parser.add_argument("--key", help="Key for cypher", required=True)

    decode_parser = subparsers.add_parser("decode", help="For command decode")
    decode_parser.set_defaults(mode="decode", func=decode)
    decode_parser.add_argument("--input_file", default=sys.stdin,
                               type=argparse.FileType("r"), help="Input file")
    decode_parser.add_argument("--output_file", default=sys.stdout,
                               type=argparse.FileType("w"), help="Output file")
    decode_parser.add_argument("--cypher",
                               choices=["caesar", "vigenere", "vernam"],
                               help="Cypher algorithm", required=True)
    decode_parser.add_argument("--key", help="Key for cypher", required=True)

    hack_parser = subparsers.add_parser("hack", help="For command hack")
    hack_parser.set_defaults(mode="hack", func=hack)
    hack_parser.add_argument("--input_file", default=sys.stdin,
                             type=argparse.FileType("r"), help="Input file")
    hack_parser.add_argument("--output_file", default=sys.stdout,
                             type=argparse.FileType("w"), help="Output file")
    hack_parser.add_argument("--cypher", choices=["caesar"],
                             help="Cypher algorithm", required=True)

    return parser


def main():
    arguments = make_parser().parse_args()

    arguments.func(arguments)


if __name__ == "__main__":
    main()
