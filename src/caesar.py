import src.symbols as symbols
import random


class CaesarCypher:

    @staticmethod
    def caesar_shift(char, key, alphabet):
        start = ord(alphabet[0])
        new_ord = (ord(char) - start + key) % len(alphabet) + start
        return chr(new_ord)

    @classmethod
    def _shift(cls, char, key):
        for _, pack in symbols.supported_symbols.items():
            if char in pack:
                return cls.caesar_shift(char, key, pack)
        return char

    @classmethod
    def encode(cls, text, key=random.randint(1, 25)):
        encoded_text = ""

        for char in text:
            encoded_text += cls._shift(char, key)

        return encoded_text

    @classmethod
    def _reverse_shift(cls, char, key):
        for _, pack in symbols.supported_symbols.items():
            if char in pack:
                return cls.caesar_shift(char, len(pack) - key, pack)
        return char

    @classmethod
    def decode(cls, text, key):
        decoded_text = ""

        for char in text:
            decoded_text += cls._reverse_shift(char, key)

        return decoded_text

    @classmethod
    def hack(cls, text):
        encoded_text = ""



        return encoded_text
