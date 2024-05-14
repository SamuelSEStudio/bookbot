def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_alpha = is_alphabetic(letter_count)
    report = convert_and_sort(letter_count_alpha)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for l in report:
        print(f"The character '{l['char']}' was found '{l['count']}' times")
    print("--- End report ---")
        
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

def is_alphabetic(lc):
    #filters out non-alphabetic characters from dictionary
    return {char: count for char, count in lc.items() if char.isalpha()}

def convert_and_sort(lca):
    #converts dict to a list of dictionaries then sorts it by count high to low
    list_of_lets = [{"char": char, "count" : count} for char, count in lca.items()]
    list_of_lets.sort(reverse=True, key = sort_on)
    return list_of_lets

def sort_on(lc):
    #return the count value for sorting
    return lc["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()