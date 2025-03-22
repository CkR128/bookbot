from stats import get_num_words, get_char_stats, sort_chars
import sys

def get_book_text(filepath):
    data = ""
    with open(filepath) as f:
        data = f.read()
    return data
def printData(path, total_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

def main(path):
    data = get_book_text(path)
    num_words = get_num_words(data)
    print(f"{num_words} words found in the document")
    num_chars = get_char_stats(data)
    print(num_chars)

    sorted = sort_chars(num_chars)
    printData("books/frankenstein.txt", num_words, sorted)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]
main(path)

