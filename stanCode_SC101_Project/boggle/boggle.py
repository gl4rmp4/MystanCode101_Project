"""
File: boggle.py
Name: Ernest_Huang
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    boggle_letter_list = []
    dict_list = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                 'l': [], 'm': [],
                 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
                 'y': [], 'z': []}
    # load the dict
    read_dictionary(dict_list)
    # boggle letter input
    for i in range(4):
        row = input(f'{i + 1} row of letter :').lower().split()
        if not judge_input(row):
            print(f'Illegal input')
            break
        elif len(row) < 4:
            print(f'Illegal input')
            break
        boggle_letter_list.append(row)
    boggle_start(boggle_letter_list, dict_list)

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def judge_input(row):
    for ele in row:
        if len(ele) != 1:
            return False
        elif not ele.isalpha():
            return False
    return True


def boggle_start(boggle_letter_list, dict_list):
    """
    :param boggle_letter_list: 記錄輸入的字母九宮格
    :param dict_list: 查核答案的字典
    :return: None
    """
    counter = [0]  # Calculate the answer str number
    total_find = []
    current_position = []
    for x in range(4):
        for y in range(4):
            boggle_start_helper(boggle_letter_list, dict_list, [], current_position, total_find, [], x, y, counter)
    print(f'There are {counter[0]} words in total.')


def boggle_start_helper(boggle_letter_list, dict_list, current_list, current_position, total_find,
                        used_position, x, y, counter):
    """
    :param boggle_letter_list: 記錄輸入的字母九宮格
    :param dict_list: 查核答案的字典
    :param current_list: 紀錄當前這在排列組合字母的list
    :param current_position: 當前排列組合中走過的4*4棋盤位置
    :param total_find: 總共找到的符合字母
    :param used_position: 紀錄已經使用過字母的位置
    :param x : int,選擇起始開頭字母的x座標
    :param y : int,選擇起始開頭字母的y座標
    :param counter : list,包含計算找到幾個答案值的list
    :return:
    """
    if len(current_list) >= 4:
        check(dict_list, current_list, total_find, counter)
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i  #
            new_y = y + j  #
            # if (new_x, new_y) not in used_position:
            if 0 <= new_x < 4 and 0 <= new_y < 4 and (new_x, new_y) not in current_position:
                if len(current_list) >= 16:
                    break
                if not has_prefix(current_list, dict_list):
                    break
                # Choose
                current_position.append((new_x, new_y))
                current_list.append(boggle_letter_list[new_y][new_x])
                # Explore
                boggle_start_helper(boggle_letter_list, dict_list, current_list, current_position,
                                    total_find, used_position, new_x, new_y, counter)
                # Un-choose
                current_list.pop()
                current_position.pop()


def check(dict_list, current_list, total_find, counter):
    """
    檢查是否有在字典裡
    :param dict_list:list,字典
    :param current_list:list,符合至少4個字母的list
    :param total_find: list,全部答案的字母list
    :param counter : list,包含計算找到幾個答案值的list
    :return:
    """
    answer_str = ''.join(current_list)
    first_letter = answer_str[0]
    for check_word in dict_list[first_letter]:
        if answer_str not in total_find:
            if answer_str == check_word:
                print(f'Found :{answer_str}')
                counter[0] += 1
                total_find.append(answer_str)
                # used_position += current_position


def read_dictionary(d):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            lines = line.strip().split('\n')
            letter = lines[0]
            first_letter = letter[0]
            d[first_letter] += lines


def has_prefix(sub_s, dict_list):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    check_str = ''.join(sub_s)
    if check_str == '':
        return True
    else:
        first_letter = check_str[0]
        for dict_str in dict_list[first_letter]:
            if dict_str.startswith(check_str):
                return True
        return False


if __name__ == '__main__':
    main()
