from typing import TypedDict


class Char(TypedDict):
    char: str
    num: int


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict[str, int]:

    chars = {}
    for word in text.split():
        for char in word:
            char = char.lower()
            # if not char.isalpha():
            #     continue
            if not char in chars:
                chars[char] = 0
            chars[char] += 1
    return chars


def get_sorted_characters(chars: dict[str, int]) -> list[Char]:
    out: list[Char] = []
    for char in sorted(chars.items(), key=lambda char: char[1], reverse=True):
        out.append({"char": char[0], "num": char[1]})
    return out
