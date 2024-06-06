"""bookbot that does something to text from books"""
def get_text(path: str) -> str:
    """returns text at a given path"""
    with open(path, encoding="UTF-8") as f:
        return f.read()

def get_word_count(text: str) -> int:
    """returns length of a text.split()"""
    return len(text.split())

def get_character_dict(text: str) -> dict[str:int]:
    """
    takes text argument, returning a alphabetically sorted 
    dictionary of how many of each alphabetical character it contains
    """
    character_dict = {}
    text = text.lower()
    for character in text:
        if not character.isalpha():
            continue
        character_dict.update({character:(character_dict.get(character, 0)+1)})
    return character_dict

def choose_sort():
    """Give the choice of numerical or alphabetical sort"""
    chosen = False
    choice = input("Do you wish to sort alphabetically, or numerically? A/N ")
    while not chosen:
        if choice.lower() == "a":
            choice = "a"
            chosen = True
            return choice

        if choice.lower() == "n":
            choice = "n"
            chosen = True
            return choice

        print("Invalid input, choose between 'A' (alphabetical) or 'N' (numerical)")


def numerical_sort(characters: dict[str:int]) -> list[dict[str:int]]:
    """returns sorted get_character_dict on its values"""
    def sort_on(d):
        return d["count"]
    sorting_list = []
    for key in characters:
        sorting_list.append({"char":key,"count":characters[key]})
    sorting_list.sort(reverse=True, key=sort_on)
    return sorting_list


def alphabetical_sort(characters: dict[str:int]) -> dict[str:int]:
    """returns sorted get_character_dict on its keys"""
    return dict(sorted(characters.items()))


def report_info(path, collection: dict[str:int] | list[dict[str:int]]):
    """
    takes alphabetically ordered dict from get_character_amount()
    and prints out how many times each character shows up
    """
    print(f"--- Begin report of {path} --- \n")
    if isinstance(collection, dict):
        for key in collection:
            print(f"'{key.upper()}' shows up {collection[key]} times")
    elif isinstance(collection, list):
        for dictionary in collection:
            print(f"'{dictionary['char'].upper()}' shows up {dictionary['count']} times")
    print("\n--- End Report ---")


def main():
    """main body for bookbot"""
    path = "books/frankenstein.txt"
    text = get_text(path)
    characters = get_character_dict(text)
    choice = choose_sort()
    if choice == "n":
        num_sorted = numerical_sort(characters)
        report_info(path, num_sorted)
    if choice == "a":
        alpha_sorted = alphabetical_sort(characters)
        report_info(path, alpha_sorted)


if __name__ == "__main__":
    main()
