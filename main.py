def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = count_words(text)
    print(f"{words} words found in the document\n")

    char_count = count_chars(text)
    char_count_list = letter_dict_to_list(char_count)
    char_count_list.sort(reverse=True, key=sort_on)
    for char in char_count_list:
        print(f"The {char['key']} character was found {char['value']} times")

def sort_on(dict):
    return dict["value"]

def count_chars(book):
    data = {}
    for letter in book:
        l = letter.lower()  
        if l in data:
            data[l] = data[l] + 1
        else:
            data[l] = 0
    return data

def letter_dict_to_list(letter_list):
    count = []
    for letter in letter_list:
        if letter.isalpha():
            count.append({"key":letter, "value": letter_list[letter]})
    return count


def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
