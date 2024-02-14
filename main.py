def main():
    file_name = "books/frankenstein.txt"
    file_contents = read_file(file_name)
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    display_report(file_name, word_count, letter_count)

def read_file(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        return file_contents

def count_words(input_str):
    return len(input_str.split())

def count_letters(input_str):
    letter_dict = {}
    for letter in input_str:
        lower_letter = letter.lower()
        if lower_letter in letter_dict:
            letter_dict[lower_letter] += 1
        else:
            letter_dict[lower_letter] = 1
    return letter_dict

def display_report(file_name, word_count, letter_dict):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print()
    sorted_letters = sort_dict(letter_dict)
    for letter in sorted_letters:
        if letter["letter"].isalpha():
            print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"letter": key, "count": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

main()
