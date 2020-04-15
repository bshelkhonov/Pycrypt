from src.caesar import CaesarCypher
import argparse
import sys

functions = {
    "encode": CaesarCypher.encode,
    "decode": CaesarCypher.decode,
    "hack": CaesarCypher.hack,
}


def read_file(file):
    return "".join(file.readlines())


def main(argv):
    parser = argparse.ArgumentParser(description="Crypt")
    parser.add_argument("mod", action="store", help="working mod - encoding")
    parser.add_argument("--input_file", help="file with text to work")
    parser.add_argument("--output_file", help="file to write result")
    parser.add_argument("--key", type=int, help="key for cypher")

    args = parser.parse_args()

    if args.input_file is None:
        text = read_file(sys.stdin)
    else:
        with open(args.input_file, "r") as f:
            text = read_file(f)

    if args.key is not None:
        processed_text = functions[args.mod](text, args.key)
    else:
        processed_text = functions[args.mod](text)

    if args.output_file is None:
        print(processed_text)
    else:
        with open(args.output_file, "w") as f:
            f.write(processed_text)


if __name__ == "__main__":
    main(sys.argv)
