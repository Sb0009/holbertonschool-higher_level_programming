#!/usr/bin/python3
"""Write a file"""


def write_file(filename='', text=''):
    """This is the write_file"""
    with open(filename, 'w+', encoding='utf-8') as file:
        return file.write(text)
