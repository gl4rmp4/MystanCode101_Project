"""
File: webcrawler.py
Name: Ernest_Huang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {"class": 't-stripe'})
        for tag in tags:
            data = tag.tbody.text
            data = data.strip()
            datas = data.split()
            man_data_list = [x for i ,x in enumerate(datas) if i%5==2]
            women_data_list = [x for i ,x in enumerate(datas) if i%5==4]
            for i in range(4):
                man_data_list.pop()
                women_data_list.pop()
            #  data list replace int type
            man_total = 0
            for i in man_data_list: # man
                replace_number = number(i)
                man_total += int(replace_number)
            women_total = 0
            for i in women_data_list:
                replace_number = number(i)
                women_total += int(replace_number)
            print('Male Number :'+str(man_total))
            print('Female Number :'+str(women_total))


def number(str_number):
    """
    give the number list
    Args:
        str_number:  str : list of webcrawler

    Returns: ans without number inside ','

    """
    # ans = ''
    # for i in range(len(str_number)):
    #     ch = str_number[i]
    #     if ch.isdigit():
    #         ans += ch
    # return ans
    # return str_number.replace(',','')  另解1

    # join
    return ''.join(str_number.split(','))



if __name__ == '__main__':
    main()
