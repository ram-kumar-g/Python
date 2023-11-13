'''A python program to find the serial numbers using regex pattern
    directory search using os.walklib
    using date time functions
    using time it and time for time counter'''


import os
import re
from datetime import *
import time


def today_date():
    print(f'Search date: {date.today().strftime('%d-%m-%Y')}')


def ser_num_finder(path):
    ser_num = r'\bN+\w{3}+\-+\d{5}'
    count = 0
    print('-'*30)
    print('| File Name\t\t|Serial number|')
    print('-' * 30)
    for fol, subfolders, files in os.walk(path):
        if files:
            for file in files:
                path = f'{fol}\\{file}'
                x = open(path)
                text = x.read()
                if re.search(ser_num,text):
                    count += 1
                    print('|', file, '\t|', re.search(ser_num, text).group(), '|')
                    print('-'*30)
    print(f'Numbers found = {count}')


def start():
    path = os.getcwd()+'\\My_Big_Directory'
    today_date()
    st = time.time()
    ser_num_finder(path)
    end = time.time()
    duration = end - st
    print(f'Search duration: {round((duration * 10), 3)} μs')


start()

