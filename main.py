from stats import count_words, count_characters, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    try:
        filepath = sys.argv[1]
        print(f"Analyzing book found at {filepath}...")
        book_text = get_book_text(filepath)
        book_word_count = count_words (book_text)
        book_char_count = count_characters(book_text)
        sorted_char_count = sort_char_count(book_text)
        print("----------- Word Count ----------")
        print(f"Found {book_word_count} total words")
        print("--------- Character Count -------")
        for entry in sorted_char_count:
            current_char = entry["char"]
            current_count = entry["num"]
            print(f"{current_char}: {current_count}")
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()