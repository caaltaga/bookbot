def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    character_count = count_letters(file_contents)
    sorted_character_count = sort_characters(character_count)
    report(word_count, sorted_character_count, path)


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(dict):
    return dict["amount"]


def sort_characters(character_count):
    sorted = []
    for character in character_count:
        char = {'character': character, 'amount': character_count[character]}
        sorted.append(char)
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def report(word_count, character_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for char in character_count:
        if char['character'].isalpha():
            print(f"The {char['character']} character was found {
                  char['amount']} times")
    print("--- End report ---")


main()
