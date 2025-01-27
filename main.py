
def count_words(txt):
    word_count = len(txt.split())
    print(word_count)
    

def count_words(txt):
    word_count = len(txt.split())
    return word_count



def get_book_text(path):
    with open(path) as f:
        return f.read()



def count_characters(txt):
    char_dict = {}

    for character in txt.lower():
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    
    return char_dict


def sort_on(dict):
    return dict['count']

def character_report(char_dict):
    char_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    for data in char_list:
        print(f"The '{data["char"]}' character was found {data["count"]} of times")



def main():

    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)

    print(f"--- Begin Report of {book_path} ---")
    print(f"{num_words} words were found in the document")
    report = character_report(chars_dict)

    

if __name__ == "__main__":
    main()

