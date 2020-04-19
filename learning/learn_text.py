import collections
import json


def _learn(text, pack_name):
    with open("./resources/symbols.json", "r") as f:
        data = json.load(f)
        alphabet = data[pack_name]

    letters_counter = collections.Counter()
    letters_number = 0

    for char in text:
        letter = char.lower()
        if letter in alphabet:
            letters_counter[letter] += 1
            letters_number += 1

    data = dict(letters_counter.most_common())

    for letter in data:
        data[letter] /= letters_number

    return data


def train(text, pack_name):
    _learn(text, pack_name)
