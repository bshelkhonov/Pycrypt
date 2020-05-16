from encryptor.caesar import CaesarCypher
from encryptor.vigenere import VigenereCypher
from encryptor.vernam import VernamCypher
from testing.testing import Testing
from learning.learn_text import Trainer
import argparse
import sys
import json
import os.path

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


def write_json(data, output_file):
    json.dump(data, output_file)


def read_json(input_file):
    return json.load(input_file)


def get_text_from_file(file):
    with open(file, "r") as f:
        return input_text(f)


def get_data_from_json(file):
    if os.path.isfile(file):
        try:
            with open(file, "r") as f:
                return read_json(f)
        except json.JSONDecodeError:
            pass
    return dict()


def write_data_to_json(data, file):
    with open(file, "w") as f:
        write_json(data, f)


def clear_file(filename):
    open(filename, "w").close()


def encode(args):
    text = input_text(args.input_file)
    try:
        key = int(args.key) if is_integer_key[args.cypher] else args.key
    except ValueError:
        print("Key must be integer")
        sys.exit(0)
    processed_text = cyphers[args.cypher].encode(text, key)
    output_text(processed_text, args.output_file)


def decode(args):
    text = input_text(args.input_file)
    key = int(args.key) if is_integer_key[args.cypher] else args.key
    processed_text = cyphers[args.cypher].decode(text, key)
    output_text(processed_text, args.output_file)


def hack(args):
    data = read_json(args.model)
    text = input_text(args.input_file)
    processed_text = cyphers[args.cypher].hack(text, data)
    output_text(processed_text, args.output_file)


def learn(args):
    text = input_text(args.input_file)
    letter_frequency, most_common_words = Trainer.train(text)
    data = {
        "l": letter_frequency,
        "w": most_common_words
    }
    write_data_to_json(data, args.output_file)


def test(args):
    Testing.run()


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
    hack_parser.add_argument("--model", type=argparse.FileType("r"),
                             help="File for hacking algorithm", required=True)
    hack_parser.add_argument("--cypher", choices=["caesar"],
                             help="Cypher algorithm", required=True)

    train_parser = subparsers.add_parser("learn",
                                         help="For learning")
    train_parser.set_defaults(mode="learn", func=learn)
    train_parser.add_argument("--input_file", default=sys.stdin,
                              type=argparse.FileType("r"), help="Input file")
    train_parser.add_argument("--output_file", help="Output file",
                              required=True)

    testing_parser = subparsers.add_parser("test", help="Run tests")
    testing_parser.set_defaults(mode="test", func=test)

    return parser


def main():
    arguments = make_parser().parse_args()

    arguments.func(arguments)


if __name__ == "__main__":
    main()
