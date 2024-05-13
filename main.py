def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(f"{word_count} words found in the {book_path}")
    print(f"{letter_count}")
        
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    for character in text.lower():
        if character not in letter_dict:
            letter_dict[character] = 1
        else:
            letter_dict[character] += 1
    return letter_dict
 

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()