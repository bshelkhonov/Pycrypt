import encryptor.symbols as symbols
import collections
import json


class Trainer:

    @staticmethod
    def _extract_word(word: str) -> str:
        return word.strip(symbols.alphabets["other"])

    @staticmethod
    def _check_language(word: str, lang: str) -> bool:
        return all(char in symbols.alphabets[lang] for char in word.lower())

    @staticmethod
    def _is_proper_name(word: str) -> bool:
        return word[0].isupper()

    @staticmethod
    def _get_current_data(file_name) -> dict:
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            return dict()

    @staticmethod
    def _write_text_in_file(text, file_name):
        with open(file_name, "w") as f:
            f.write(text)

    @staticmethod
    def _write_in_json(data, file_name):
        with open(file_name, "w") as f:
            json.dump(data, f)

    @classmethod
    def _add_in_json(cls, key, data, file_name):
        current_data = cls._get_current_data(file_name)
        current_data[key] = data
        with open(file_name, "w") as f:
            json.dump(current_data, f)

    @staticmethod
    def calculate_letters_frequency(text, pack_name):
        alphabet = symbols.alphabets[pack_name]

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

    @classmethod
    def find_most_common_words(cls, text, pack_name):
        TOP_PERCENT = 0.08
        MIN_WORD_LEN = 3

        words_counter = collections.Counter()

        def is_normal_word(w: str) -> bool:
            return len(w) >= MIN_WORD_LEN and \
                   cls._check_language(w, pack_name) and \
                   not cls._is_proper_name(w)

        for word in text.split():
            word = cls._extract_word(word)

            if is_normal_word(word):
                words_counter[word] += 1

        top_words_num = int(len(words_counter) * TOP_PERCENT)

        data = [word[0] for word in words_counter.most_common(top_words_num)]

        return data
