import data
from typing import Optional

# Write your functions for each part in the space below.
# part 1
# The following function takes an input list of books of class book and performs the selection sort algorithm,
# sorting the books by alphabetical order of title. The output is a list of titles in alphabetical order.
def selection_sort_books(book_list):
    for i in range(len(book_list)):
        lowest_index = i
        for j in range(i + 1, len(book_list)):
            if book_list[j].title < book_list[lowest_index].title:
                lowest_index = j
        if lowest_index != i:
            temp = book_list[i]
            book_list[i] = book_list[lowest_index]
            book_list[lowest_index] = temp
    return [book.title for book in book_list]

# Part 2
# The following function takes an input string and makes all its lower case letters uppercase and
# vice versa. The output it returns is a string with the cases switched as described.
def swap_case(string):
    def switch_case(letter):
        if letter.isupper():
            return letter.lower()
        else:
            return letter.upper()
    final_letters = [switch_case(letter) for letter in string]
    return ''.join(final_letters)
# Part 3
# The following function takes a string and two letters as the input. Then, the function replaces all
# instances of the first letter in the string with the second letter. The output of the function
# is the new string modified as described.
def str_translate(string, first_letter, second_letter):
    def switch_letter(letter, letter1, letter2):
        if letter == letter1:
            return letter2
        else:
            return letter
    letter1 = first_letter
    letter2 = second_letter
    final_letters = [switch_letter(letter, letter1, letter2) for letter in string]
    return ''.join(final_letters)
# Part 4
# The following function takes a string of at least one word as the input, splits the string up into
# individual words, and gradually creates a dictionary with every word that occurs in the string and
# its count (how many times it appears in the string). The output is the final dictionary with all the
# unique words in the string and their count.
def histogram(strings):
    word_count = {}
    words = strings.split()
    for i in range(len(words)):
        if words[i] in word_count:
            word_count[words[i]] += 1
        else:
            word_count[words[i]] = 1
    return word_count
