def count_words(text):

    words = text.split()
    print(f"Word Count: {len(words)}")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)


main()
