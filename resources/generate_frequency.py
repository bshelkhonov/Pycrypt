import unicodedata
import collections
import json


def _generate(input_file, pack_name):
    PACK_SUFFIX = "_lowercase"

    with open("symbols.json", "r") as f:
        data = json.load(f)
        alphabet = data[pack_name + PACK_SUFFIX]

    letters_counter = collections.Counter()
    letters_number = 0
    for line in input_file:
        for char in line:
            letter = char.lower()
            if letter in alphabet:
                letters_counter[letter] += 1
                letters_number += 1

    data = dict(letters_counter.most_common(len(alphabet) // 2))

    for letter in data:
        data[letter] /= letters_number

    return data


def _main():
    INPUT_FILE = "text_for_learning_{}.txt"

    packs = ("eng", "rus")

    data = dict()

    for pack in packs:
        with open(INPUT_FILE.format(pack), "r") as input_file:
            data_for_pack = _generate(input_file, pack)
        data[pack] = data_for_pack

    with open("letter_frequencies.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    _main()
