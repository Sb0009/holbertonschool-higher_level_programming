#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """This is the read_file method"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
