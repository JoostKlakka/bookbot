def main():
    book = "books/frankenstein.txt"    
    with open(book) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        print(f"----------------------------------")
        print(f"- {book}")
        print(f"----------------------------------")
        print(f"- words:   {words}")
        print(f"----------------------------------")
        print_letters(file_contents)
        print(f"----------------------------------")

def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    lowered_book = book.lower()
    book_letters = {}
    for letter in alfabet_list:
        book_letters[letter] = 0
    for letter in lowered_book:
        for a_letter in alfabet_list:
            if a_letter == letter:
                book_letters[letter] += 1
    return book_letters

def print_letters(file_contents):
    letters = count_letters(file_contents)
    for letter in letters:
            print(f"- {letter} count {letters[letter]}")    

#Setup Variables:
alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabet_list = []
for letter in alfabet:
    alfabet_list.append(letter)

main()