#!/usr/bin/python3
"""Module to create a class
"""


class Square:
    """This is a square class
    """

    def __init__(self, size=0):
        """this is a __init__ method
        Is to initianilize the variables
        Args:
           size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """this is a size method
        Is to get the size of the square
        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a size method
        Is to set the value of the square's size
        Args:
            value (int): new size of the square
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """This is a area method
        Is to calculate the area of the square
        Returns:
            The square's area
        """
        return self.__size ** 2

    def my_print(self):
        """this is a my_print method
        Is to print a square with #
        """
        if (self.__size == 0):
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end='')
            print()
