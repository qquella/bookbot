import re


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    sorted_dict = dict(sorted(chars_dict.items()))

    for k in sorted_dict:
        pattern = re.compile("[a-z]")
        if pattern.match(k) != None:
            print(f"The '{k}' character was found {chars_dict[k]} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_char_count(str):
    result = {}
    str = str.lower()
    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


main()
