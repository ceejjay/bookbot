def word_count(str) -> int:
    words = str.split()
    return(len(words))

def letter_count(str) -> dict:
    letter_count = dict()
    for letter in str.lower():
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter,0) + 1  
    return dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))

def print_report(book:str): 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book)} words found in the document")
    for k,v in letter_count(book).items():
        print(f"The '{k}' character was found {v} times")

def main() -> int:
    with open("./books/frankenstein.txt") as f:
        print_report(f.read())
main()