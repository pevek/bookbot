def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = count_characters(text)
    characters.sort(key=sort_on, reverse=True)
    word_count = get_num_words(text)
    print_report(characters, book_path, word_count)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]

def count_characters(text):
    characters = {}
    letters = text.lower()
    for letter in letters:
        if letter.isalpha():
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    character_list = [{'char': char, 'num': count} for char, count in characters.items()]
    return character_list

def print_report(characters, title, word_count):
    print(f"--- Begin report of {title} ---")
    print(f"{word_count} words in the document\n")
    for c in characters:
        print(f"The '{c['char']}' character was found {c['num']} times.")
    print("--- End report ---")


main()
