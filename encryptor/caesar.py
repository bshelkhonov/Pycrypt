import encryptor.symbols as symbols
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
    def letter_loss(cls, text, proba_data):

        letters_counter = dict()
        letters_number = collections.Counter()

        for pack in proba_data:
            letters_counter[pack] = collections.Counter()

        for char in text:
            letter = char.lower()
            for pack in proba_data:
                if letter in symbols.alphabets[pack]:
                    letters_number[pack] += 1
                if letter in proba_data[pack]:
                    letters_counter[pack][letter] += 1

        score = 0

        for pack in letters_counter:
            data = dict(letters_counter[pack])

            for letter in data:
                freq_cur = data[letter] / letters_number[pack]
                freq_orig = proba_data[pack][letter]
                score += (freq_cur - freq_orig) ** 2

        return score

    @classmethod
    def word_loss(cls, text, word_data):
        word_match = 0

        for word in text.split():
            word = cls._extract_word(word).lower()

            for pack in word_data:
                if word in word_data[pack]:
                    word_match += 1
                    break

        return -word_match

    @classmethod
    def hack(cls, text, proba_data, words_data):
        MIN_TEXT_LENGTH = 5000
        KEY_VARIANTS = 51

        best_variant = (math.inf, -1)

        if words_data is not None and len(text) < MIN_TEXT_LENGTH:
            loss_fn = cls.word_loss
            data = words_data
        else:
            print("HERE")
            loss_fn = cls.letter_loss
            data = proba_data

        for key in range(KEY_VARIANTS):
            decoded = cls.decode(text, key)
            best_variant = min((loss_fn(decoded, data), key), best_variant)

        return cls.decode(text, best_variant[1])
