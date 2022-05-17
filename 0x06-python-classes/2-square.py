#!/usr/bin/python3
"""Module to create a class
"""


class Square:
    """This is a Square class
    """

    def __init__(self, size=0):
        """This is the __init__ method
        Args:
            size (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
