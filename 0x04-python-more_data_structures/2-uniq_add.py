#!/usr/bin/python3
'''
    Write a function that adds all unique integers in a list (only once for each integer).
'''


def uniq_add(my_list=[]):

    total = 0

    for number in set(my_list):
        total += number

    return total
