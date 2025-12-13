from stats import text_to_list, char_count, sorting_dict, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    if len(sys.argv) != 2:  # if the input doesn't have a length of two return.
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    filepath1 = filepath[1]
    text = get_book_text(filepath1)
    text_list = text_to_list(text)
    num_words = len(text_list)
    char_dict = char_count(text_list)
    sort_dict = sorting_dict(char_dict)
    sort_dict.sort(reverse=True, key=sort_on)
    print(f"Found {num_words} total words")
    for entry in sort_dict:
        if entry["chara"].isalpha() == True:
            print(f"{entry["chara"]}: {entry["count"]}")
    return



main(sys.argv)

