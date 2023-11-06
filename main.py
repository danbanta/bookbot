def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents)
    letter_count = get_letter_count(file_contents)
    letters_sorted_list = convert_dict_to_sorted_list(letter_count)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for item in letters_sorted_list:
        print(f"The {item['letter']} character was found {item['number']} times")
    print(f"--- End report ---")

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_letter_count(file_contents):
    letter_dict = {}
    letters = file_contents.lower()
    for letter in letters:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

def sort(dict):
    return dict["number"]

def convert_dict_to_sorted_list(dict):
    letter_list = []
    for letter in dict:
        letter_list.append({"letter": letter, "number": dict[letter]})
    letter_list.sort(reverse=True, key=sort)
    return letter_list

main()
