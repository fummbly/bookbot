def count_words(text):

    words = text.split()
    return len(words)


def sort_on(dict):
    return dict["Num"]


def chars_dict_to_sorted_list(num_chars_list):
    sorted_list = []
    for char in num_chars_list:
        sorted_list.append({"Char": char, "Num": num_chars_list[char]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_chars(text):

    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {file_path}")
    print(f"{num_words} words found in the document")
    print()

    for char in chars_sorted_list:
        if not char["Char"].isalpha():
            continue
        print(f"The '{char["Char"]}' character was found {char['Num']} times")
    print("--- End report ---")


main()
