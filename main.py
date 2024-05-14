def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_dict = [{"char": char, "count": count} for char, count in letter_count.items() if char,isalpha()]
    letter_count_dict.sort(reverse=True, key = sort_on)
    print(f"{word_count} words found in the {book_path}")
    print(f"{letter_count_dict}")
        
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

def sort_on(letter_count):
    if letter_count["char"].isalpha():
        return letter_count["count"]
    else: 
        return 0

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()