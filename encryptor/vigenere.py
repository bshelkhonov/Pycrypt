from encryptor.symbols import vigenere_alphabet


class VigenereCypher:
    alphabet_set = set(vigenere_alphabet)

    @staticmethod
    def _process_char(char, key_char, reverse: bool = False):
        pos_char = vigenere_alphabet.index(char)
        pos_key = vigenere_alphabet.index(key_char)
        if reverse:
            pos_new_char = (pos_char - pos_key + len(vigenere_alphabet)) % len(
                vigenere_alphabet)
        else:
            pos_new_char = (pos_char + pos_key) % len(vigenere_alphabet)
        return vigenere_alphabet[pos_new_char]

    @classmethod
    def encode(cls, text, key: str):
        if len(key) < len(text):
            key *= len(text) // len(key)
            key += key[:len(text) - len(key)]

        encoded_text = ""

        for index, char in enumerate(text):
            if char in cls.alphabet_set:
                encoded_text += cls._process_char(char, key[index])
            else:
                encoded_text += char
        return encoded_text

    @classmethod
    def decode(cls, text, key: str):
        if len(key) < len(text):
            key *= len(text) // len(key)
            key += key[:len(text) - len(key)]

        decoded_text = ""

        for index, char in enumerate(text):
            if char in cls.alphabet_set:
                decoded_text += cls._process_char(char, key[index], True)
            else:
                decoded_text += char

        return decoded_text
