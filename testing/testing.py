from encryptor.caesar import CaesarCypher
from encryptor.vigenere import VigenereCypher
from encryptor.vernam import VernamCypher
import random


class Testing:
    _test_files = ("./testing/tests/text_1.txt",
                   "./testing/tests/text_2.txt",
                   "./testing/tests/text_3.txt",
                   "./testing/tests/text_4.txt")

    @staticmethod
    def _get_text_from_file(file_name: str) -> str:
        with open(file_name, "r") as f:
            return "".join(f.readlines())

    @staticmethod
    def _test_encode(cypher, text, key):
        temp = cypher.encode(text, key)
        assert temp != text
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
        no_errors = True
        for test_file in cls._test_files:
            text = cls._get_text_from_file(test_file)
            try:
                cls._test_encode(CaesarCypher, text, random.randint(1, 10))
            except AssertionError:
                no_errors = False
                print(f"Caesar test failed - encoding, decoding: {test_file}")

        if no_errors:
            print("Successfully passed encoding/decoding test")

        print("Running Caesar hacking test")
        no_errors = True
        for test_file in cls._test_files:
            text = cls._get_text_from_file(test_file)
            try:
                cls._test_hack(CaesarCypher, text, random.randint(1, 10))
            except AssertionError:
                no_errors = False
                print(f"Caesar hacking test failed: {test_file}")
        if no_errors:
            print("Successfully passed Caesar hacking test")

    @classmethod
    def _test_vigenere(cls):
        print("Running Vigenere encoding/decoding test")
        no_errors = True
        for test_file in cls._test_files:
            text = cls._get_text_from_file(test_file)
            try:
                cls._test_encode(VigenereCypher, text, "banana")
            except AssertionError:
                no_errors = False
                print(f"Vigenere encoding/decoding test failed: {test_file}")
        if no_errors:
            print("Successfully passed encoding/decoding test")

    @classmethod
    def _test_vernam(cls):
        print("Running Vigenere encoding/decoding test")
        no_errors = True
        for test_file in cls._test_files:
            text = cls._get_text_from_file(test_file)
            key = VigenereCypher.encode(text, "pineapple")
            try:
                cls._test_encode(VernamCypher, text, key)
            except AssertionError:
                no_errors = False
                print("Vernam encoding/decoding test failed")
        if no_errors:
            print("Successfully passed encoding/decoding test")

    @classmethod
    def run(cls):
        cls._test_caesar()
        cls._test_vigenere()
        cls._test_vernam()
