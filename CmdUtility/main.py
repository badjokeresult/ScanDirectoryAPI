import requests
import os
import regex as re
from time import time
from APIWorker import APIWorker


def main():
    while True:
        for key, value in APIWorker.menu:
            print(f'{key}. {value}')
        option = None
        try:
            option = int(input('Choose the menu option: '))
            assert option in range(1, 7)
        except ValueError:
            print('Invalid input, retry')
            continue
        except AssertionError:
            print('Option is not in menu range, retry')
            continue
        if option == 1:
            create_scan_task()
        elif option == 2:
            update_scan_task()
        elif option == 3:
            delete_scan_task()
        elif option == 4:
            get_scan_task()
        elif option == 5:
            get_scan_tasks()
        else:
            print('Quitting the program...')
            input()
            return


def create_scan_task():
    try:
        path = get_path()


def get_path():
    pattern = r'\w+:\\(\w+|\\)+'
    path = input('Enter the directory path: ')
    if not re.match(pattern, path):
        raise ValueError
    return path


def get_