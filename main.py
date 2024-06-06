"""bookbot that does something to text from books"""
def get_text(path: str) -> str:
    """returns text at a given path"""
    with open(path, encoding="UTF-8") as f:
        return f.read()

def get_word_count(text: str) -> int:
    """returns length of a text.split()"""
    return len(text.split())

def alphabetical_sort(text: str) -> dict[str:int]:
    """
    takes text argument, returning a alphabetically sorted 
    dictionary of how many of each alphabetical character it contains
    """
    character_dict = {}
    text = text.lower()
    for character in text:
        if character.isalpha():
            character_dict.update({character:(character_dict.get(character, 0)+1)})
    alpha_sort = dict(sorted(character_dict.items()))
    return alpha_sort

# def numerical_sort(text: str) -> list[dict[str:int]]:
#     text = text.lower()
#     for character in text:
        
#     alpha_sort = dict(sorted(character_dict.items()))
#     return alpha_sort

def report_info(path, dictionary: dict[str:int]):
    """
    takes alphabetically ordered dict from get_character_amount()
    and prints out how many times each character shows up
    """
    print(f"--- Begin report of {path} --- \n")
    sorted_dict = dictionary
    for key in sorted_dict:
        print(f"'{key.upper()}' shows up {sorted_dict[key]} times")
    print("\n--- End Report ---")


def main():
    """main body for bookbot"""
    path = "books/frankenstein.txt"
    text = get_text(path)
    
    characters = alphabetical_sort(text)
    report_info(path, characters)


if __name__ == "__main__":
    main()
