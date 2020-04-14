import src.symbols as symbols
import random
import unicodedata


class CaesarCypher:
    _punctuation_set = set(symbols.punctuation)

    @staticmethod
    def caesar_shift(char, key, alphabet=symbols.ascii_lowercase):
        start = ord(alphabet[0])
        new_ord = (ord(char) - start + key) % len(alphabet) + start
        return chr(new_ord)

    @classmethod
    def _shift_ascii(cls, char, key):
        if key in symbols.ascii_lowercase:
            alphabet = symbols.ascii_lowercase
        else:
            alphabet = symbols.ascii_uppercase
        return cls.caesar_shift(char, key, alphabet)

    @classmethod
    def _shift_cyrillic(cls, char, key):
        if key in symbols.cyrillic_lowercase:
            alphabet = symbols.cyrillic_lowercase
        else:
            alphabet = symbols.cyrillic_uppercase
        return cls.caesar_shift(char, key, alphabet)

    @classmethod
    def _shift_punctuation(cls, char, key):
        return cls.caesar_shift(char, key, symbols.punctuation)

    @classmethod
    def _shift(cls, char, key):
        if char in symbols.ascii_letters:
            return cls._shift_ascii(char, key)

        elif char in symbols.cyrillic_letters:
            return cls._shift_cyrillic(char, key)

        elif char in symbols.punctuation(char, key):
            return cls._shift_punctuation(char, key)

    @classmethod
    def encode(cls, text, key=random.randint(1, 25)):
        encoded_text = ""

        for char in text:
            encoded_text += cls._shift(char, key)

        return encoded_text

    @classmethod
    def _reverse_shift(cls, char, key):
        if char in symbols.ascii_letters:
            return cls._shift_ascii(char, len(symbols.ascii_lowercase) - key)

        elif char in symbols.cyrillic_letters:
            return cls._shift_cyrillic(char,
                                       len(symbols.cyrillic_lowercase) - key)

        elif char in symbols.punctuation(char, key):
            return cls._shift_punctuation(char, len(symbols.punctuation) - key)

    @classmethod
    def decode(cls, text, key):
        decoded_text = ""

        for char in text:
            decoded_text += cls._reverse_shift(char, key)

        return decoded_text
