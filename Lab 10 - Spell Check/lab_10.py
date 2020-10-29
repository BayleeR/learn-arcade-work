import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    dictionary_file = open("dictionary.txt")

    # Create an empty list to store our names
    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    dictionary_file.close()

    # -- Linear Search --

    alice_text = open("AliceInWonderLand200.txt")

    line_count = 0
    print()
    print("Linear Search")
    print()
    # goes through each line of a list
    for line in alice_text:
        word_list = split_line(line)
        line_count += 1
        # goes through each word of a list
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                # Advance to the next item in the list
                current_list_position += 1
            if current_list_position == len(dictionary_list):
                print("Possible misspelled word", word, "on line", line_count)

    alice_text.close()

    # -- Binary Search --

    alice_text = open("AliceInWonderLand200.txt")

    line_number = 0
    print()
    print("Binary Search")
    print()
    for line in alice_text:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Possible misspelled word", word, "on line", line_number)
main()

