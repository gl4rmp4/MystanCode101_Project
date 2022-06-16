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
FIND_WORD = []


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator "(or -1 to quit)')
    s = input('Find anagrams for : ').lower()
    read_dictionary()
    find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global FIND_WORD
    with open(FILE, 'r') as f:
        for line in f:
            lines = line.strip().split('\n')
            FIND_WORD += lines
    # print(FIND_WORD)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    find_anagrams_helper(s, FIND_WORD, [])



def find_anagrams_helper(user_string, dict_list, current_list):
    if user_string == EXIT:
        pass
    else:
        print('Search ...')
        for word in dict_list:
            if len(word) == len(user_string) and sorted(word) == sorted(user_string):
                print(word)
                current_list.append(word)
                print('Search ...')
        print(current_list)
        current_list = []
        user_string = input('Find anagram for :').lower()
        # Explore
        find_anagrams_helper(user_string, dict_list, current_list)



def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
