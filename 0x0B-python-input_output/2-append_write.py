#!/usr/bin/python3
"""append and write a file"""


def append_write(filename='', text=''):
    """This is the append_write method"""
    with open(filename, 'a+', encoding='utf-8') as file:
        return file.write(text)
