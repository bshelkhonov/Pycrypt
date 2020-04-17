class VernamCypher:

    @staticmethod
    def _make_xor(a, b):
        return chr(ord(a) ^ ord(b))

    @classmethod
    def encode(cls, text, key):
        if len(text) != len(key):
            raise ValueError("Text and key must have same length")

        encoded_text = ""

        for index, char in enumerate(text):
            encoded_text += cls._make_xor(char, key[index])

        return encoded_text

    decode = encode
