#!/usr/bin/python3
"""Module to create
"""


class Square:
    """this is a Square class
    """

    def __init__(self, size=0):
        """this is the __init__ method
        Args:
           size (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """This is area method
        Is to calculate the are of the square
        Returns:
           The are of the square
        """
        return self.__size ** 2
