def count_words(text):

    words = text.split()
    print(f"Word Count: {len(words)}")
    return words


def count_letters(words):
    letters = {}
    for word in words:
        letter_list = list(word)
        for letter in letter_list:
            lower_letter = letter.lower()
            if (lower_letter in letters):
                letters[lower_letter] += 1
            else:
                letters[lower_letter] = 1

    print(f"Letter Dict: {letters}")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        count_letters(words)


main()
