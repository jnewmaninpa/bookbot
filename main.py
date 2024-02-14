def main():
    file_contents = read_file()
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the file")
    letter_count = count_letters(file_contents)
    print(f"Letter count: {letter_count}")
    
def read_file():
    with open("books/frankenstein.txt") as f:
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

main()
