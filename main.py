import sys

def main():
    
    file_contents = ""
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    words = file_contents.split()
    print(f"{len(words)}  words found in the document")
    
    chars = {}
    for word in words:
        for char in word:
            char = char.lower()
            if not char.isalpha():
                continue
            if not char in chars:
                chars[char] = 0
            chars[char] += 1
    
    for char in sorted(chars.items(), key=lambda char: char[1], reverse=True):
        print(f"The '{char[0]}' character was found {char[1]} times")

if __name__ == '__main__':
    sys.exit(main())