"""
File: largest_digit.py
Name: Ernest_Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n:
    :return:
    """
    max_number = 0
    current_number = abs(n)%10
    max_number = find_largest_digit_helper(n, max_number,current_number)
    return max_number


def find_largest_digit_helper(n, max_number,current_number):
    if int(n) > 0:
        max_number = n % 10
        if current_number > max_number:
            max_number = current_number
        else:
            current_number = max_number
        n //= 10
        return find_largest_digit_helper(n, max_number,current_number)
    elif n == 0:
        return max_number
    else:
        return find_largest_digit_helper(abs(n), max_number,current_number)


if __name__ == '__main__':
    main()
