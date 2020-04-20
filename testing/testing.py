from encryptor.caesar import CaesarCypher
from encryptor.vigenere import VigenereCypher
from encryptor.vernam import VernamCypher
import random


class Testing:
    _test_files = ("./testing/tests/text_1.txt", "./testing/tests/text_2.txt")

    @staticmethod
    def _get_text_from_file(file_name: str) -> str:
        with open(file_name, "r") as f:
            return "".join(f.readlines())

    @staticmethod
    def _test_encode(cypher, text, key):
        temp = cypher.encode(text, key)
        temp = cypher.decode(temp, key)
        assert text == temp

    @staticmethod
    def _test_hack(cypher, text, key):
        encoded = cypher.encode(text, key)
        hacked = cypher.hack(encoded)
        assert text == hacked

    @classmethod
    def _test_caesar(cls):
        print("Running Caesar encoding/decoding test")
        try:
            for test_file in cls._test_files:
                text = cls._get_text_from_file(test_file)
                cls._test_encode(CaesarCypher, text, random.randint(1, 10))
        except AssertionError:
            print("Caesar test failed - encoding, decoding")
        else:
            print("Successfully passed encoding/decoding test")

        print("Running Caesar hacking test")
        try:
            for test_file in cls._test_files:
                text = cls._get_text_from_file(test_file)
                cls._test_hack(CaesarCypher, text, random.randint(1, 10))
        except AssertionError:
            print("Caesar hacking test failed")
        else:
            print("Successfully passed hacking test")

    @classmethod
    def _test_vigenere(cls):
        print("Running Vigenere encoding/decoding test")
        try:
            for test_file in cls._test_files:
                text = cls._get_text_from_file(test_file)
                cls._test_encode(VigenereCypher, text, "banana")
        except AssertionError:
            print("Vigenere encoding/decoding test failed")
        else:
            print("Successfully passed encoding/decoding test")

    @classmethod
    def _test_vernam(cls):
        print("Running Vigenere encoding/decoding test")
        try:
            for test_file in cls._test_files:
                text = cls._get_text_from_file(test_file)
                key = VigenereCypher.encode(text, "pineapple")
                cls._test_encode(VernamCypher, text, key)
        except AssertionError:
            print("Vigenere encoding/decoding test failed")
        else:
            print("Successfully passed encoding/decoding test")

    @classmethod
    def run(cls):
        cls._test_caesar()
        cls._test_vigenere()
        cls._test_vernam()
