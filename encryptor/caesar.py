import resources.symbols as symbols
import random
import math
import collections


class CaesarCypher:

    @staticmethod
    def _extract_word(word: str) -> str:
        return word.strip(symbols.alphabets["other"])

    @staticmethod
    def caesar_shift(char, key: int, alphabet: str):
        index = alphabet.index(char)
        new_index = (index + key) % len(alphabet)
        return alphabet[new_index]

    @classmethod
    def _shift(cls, char, key: int, reverse: bool = False):
        letter = char.lower()
        for pack in symbols.alphabets:
            if letter in symbols.alphabets[pack]:
                alphabet = symbols.alphabets[pack]

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

    @classmethod
    def letter_loss(cls, text):

        letters_counter = collections.Counter()
        letters_number = 0

        for char in text:
            letter = char.lower()
            for pack in symbols.symbol_frequency:
                if letter in symbols.alphabets[pack]:
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
    def word_loss(cls, text):
        word_match = 0

        for word in text.split():
            word = cls._extract_word(word).lower()

            for pack in symbols.most_common_words:
                if word in symbols.most_common_words[pack]:
                    word_match += 1
                    break

        return -word_match

    @classmethod
    def hack(cls, text):
        MIN_TEXT_LENGTH = 5000
        KEY_VARIANTS = 50

        best_variant = (math.inf, -1)

        if len(text) < MIN_TEXT_LENGTH:
            loss_fn = cls.word_loss
        else:
            loss_fn = cls.letter_loss

        for key in range(KEY_VARIANTS):
            decoded = cls.decode(text, key)
            best_variant = min((loss_fn(decoded), key), best_variant)

        return cls.decode(text, best_variant[1])
