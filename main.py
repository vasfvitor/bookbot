def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = count_words(text)
    print(f"{words} words found in the document\n")

    char_count = count_chars(text)
    table = char_count.sort(reverse=True, key=sort_on)
    print(table)

def sort_on(dict):
    print(dict)
    return dict["value"]

def count_chars(book):
    count = []
    for letter in book:
        data = {}
        l = letter.lower()
        if l in count:
            print(l)       
            data.update({"value": count[l]+ 1})
        else:
            if l.isalpha():
                data = {"key": l, "value": 0}
                count.append(data)
        # if data not in count:
    return count


def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
