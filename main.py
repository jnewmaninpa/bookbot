def main():
    file_contents = read_file()
    word_count = count_words(file_contents)
    print(word_count)
    
def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def count_words(input_str):
    return len(input_str.split())

main()
