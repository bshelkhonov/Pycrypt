from encryptor.caesar import CaesarCypher
from encryptor.vigenere import VigenereCypher
from encryptor.vernam import VernamCypher
import learning.learn_text as trainer
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


def get_text_from_file(file):
    with open(file, "r") as f:
        return input_text(f)


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
    text = input_text(args.input_file)
    processed_text = cyphers[args.cypher].hack(text)
    output_text(processed_text, args.output_file)


def train(args):
    text = input_text(args.input_file)
    trainer.train(text, args.pack)
    print(f"Trained {args.pack} language")


def reset(args):
    trainer.train(
        get_text_from_file("resources/text_for_learning_eng.txt"), "eng")
    trainer.train(
        get_text_from_file("resources/text_for_learning_rus.txt"), "rus")


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

    train_parser = subparsers.add_parser("train", help="For training")
    train_parser.set_defaults(mode="train", func=train)
    train_parser.add_argument("--pack", choices=["eng", "rus"],
                              help="Language", required=True)
    train_parser.add_argument("--input_file", type=argparse.FileType("r"),
                              help="Input file", required=True)

    reset_parser = subparsers.add_parser("reset", help="For reset")
    reset_parser.set_defaults(mode="reset", func=reset)

    return parser


def main():
    arguments = make_parser().parse_args()

    arguments.func(arguments)


if __name__ == "__main__":
    main()
