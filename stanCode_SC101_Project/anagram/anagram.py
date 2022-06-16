"""
File: anagram.py
Name: Ernest_Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
# Global variable
FIND_WORD = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [],
             'm': [], 'n': [], 'o': [],
             'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator "(or -1 to quit)')
    read_dictionary()
    while True:
        s = input('Find anagrams for : ').lower()
        if s == EXIT:
            break
        find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    give the dictionary classification
    """
    global FIND_WORD
    with open(FILE, 'r') as f:
        for line in f:
            lines = line.strip().split('\n')
            letter = lines[0]
            first_letter = letter[0]
            FIND_WORD[first_letter] += lines


def find_anagrams(s):
    """
    :param s: str,user input string
    :return: None
    """
    ans_list = []
    find_anagrams_helper(len(s), '', s, ans_list, '')
    print(f'{len(ans_list)} anagram {ans_list}')


def find_anagrams_helper(target_len, current_string, user_string, ans_list, user_string_first_letter):
    """
    :param target_len: int,user input string len
    :param current_string: str,permutations the string
    :param user_string: str,user input string to check answer
    :param ans_list: list, every answer string
    :param user_string_first_letter: str, user input string first letter
    :return:
    """
    if current_string == '':
        pass
    else:
        user_string_first_letter = current_string[0]
    if sorted(current_string) == sorted(user_string):
        if current_string in FIND_WORD[user_string_first_letter]:
            if current_string not in ans_list:
                ans_list.append(current_string)
                print('Searching ...')
                print(f'Found : {current_string}')
    else:
        for i in user_string:
            if len(current_string) >= target_len:
                break
            # Choose
            if not has_prefix(current_string):
                break
            current_string += i
            # Explore
            find_anagrams_helper(target_len, current_string, user_string, ans_list, user_string_first_letter)
            # Un-choose
            current_string = current_string[:-1]


def has_prefix(sub_s):
    """
    主要減少探索的時間
    :param sub_s:
    :return:
    """
    if sub_s == '':
        return True
    else:
        s_first = sub_s[0]
        for dict_str in FIND_WORD[s_first]:
            if dict_str.startswith(sub_s):
                return True
        return False


if __name__ == '__main__':
    main()
