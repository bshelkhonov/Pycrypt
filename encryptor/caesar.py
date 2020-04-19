import resources.symbols as symbols
import random
import math
import collections


class CaesarCypher:

    @staticmethod
    def caesar_shift(char, key: int, alphabet: str):
        index = alphabet.index(char)
        new_index = (index + key) % len(alphabet)
        return alphabet[new_index]

    @classmethod
    def _shift(cls, char, key: int, reverse: bool = False):
        letter = char.lower()
        for pack in symbols.caesar_symbols:
            if letter in symbols.caesar_symbols[pack]:
                alphabet = symbols.caesar_symbols[pack]

                if reverse:
                    key = len(alphabet) - key
                new_letter = cls.caesar_shift(letter, key, alphabet)

                return new_letter.upper() if char.isupper() else new_letter
        return char

    @classmethod
    def encode(cls, text, key: int = random.randint(1, 25)):
        encoded_text = ""

        for char in text:
            encoded_text += cls._shift(char, key)

        return encoded_text

    @classmethod
    def decode(cls, text, key: int):
        decoded_text = ""

        for char in text:
            decoded_text += cls._shift(char, key, True)

        return decoded_text

    @staticmethod
    def _get_score(text):

        letters_counter = collections.Counter()
        letters_number = 0

        for char in text:
            letter = char.lower()
            for pack in symbols.symbol_frequency:
                if letter in symbols.caesar_symbols[pack]:
                    letters_number += 1
                if letter in symbols.symbol_frequency[pack]:
                    letters_counter[letter] += 1

        data = dict(letters_counter)
        score = 0
        for letter in data:
            for pack in symbols.symbol_frequency:
                if letter in symbols.symbol_frequency[pack]:
                    freq_cur = data[letter] / letters_number
                    freq_orig = symbols.symbol_frequency[pack][letter]
                    score += (freq_cur - freq_orig) ** 2

        return score

    @classmethod
    def hack(cls, text):
        best_variant = (math.inf, -1)

        for key in range(30):
            decoded = cls.decode(text, key)
            best_variant = min((cls._get_score(decoded), key), best_variant)

        return cls.decode(text, best_variant[1])
