import sys

from stats import count_characters, count_words, get_sorted_characters


def main():

    print("============ BOOKBOT ============")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    print(f"Analyzing book found at {filename}...")

    file_contents = get_book_text(filename)

    print("----------- Word Count ----------")

    num_words = count_words(file_contents)

    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    chars = get_sorted_characters(count_characters(file_contents))

    for item in chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(filename: str) -> str:

    file_contents: str = ""
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    sys.exit(main())
