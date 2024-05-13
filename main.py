def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"{word_count} words found in the {book_path}")
        
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()