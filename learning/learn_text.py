import resources.symbols as symbols
import collections
import json


def _extract_word(word: str) -> str:
    return word.strip(symbols.alphabets["other"])


def _check_language(word: str, lang: str) -> bool:
    return all(char in symbols.alphabets[lang] for char in word.lower())


def _is_proper_name(word: str) -> bool:
    return word[0].isupper()


def _learn_letter_frequencies(text, pack_name):
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

    with open("resources/letter_frequencies.json", "w") as f:
        json.dump(data, f)


def _learn_most_common_words(text, pack_name):
    TOP_PERCENT = 0.08
    MIN_WORD_LEN = 4

    words_counter = collections.Counter()
    words_number = 0

    def is_normal_word(w: str) -> bool:
        return len(w) >= MIN_WORD_LEN and \
               _check_language(w, pack_name) and \
               not _is_proper_name(w)

    for word in text.split():
        word = _extract_word(word)

        if is_normal_word(word):
            words_counter[word] += 1
            words_number += 1

    top_words_num = int(len(words_counter) * TOP_PERCENT)

    data = dict(words_counter.most_common(top_words_num))
    for word, _ in words_counter.most_common(10):
        print(word)

    for word in data:
        data[word] /= words_number

    with open("resources/most_common_words.json", "w") as f:
        json.dump(data, f)


def train(text: str, pack_name: str):
    _learn_letter_frequencies(text, pack_name)
    _learn_most_common_words(text, pack_name)
