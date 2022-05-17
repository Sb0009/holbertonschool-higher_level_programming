#!/usr/bin/python3
"""Module to create a class
"""


class Square:
    """this is a Square class
    """

    def __init__(self, size=0):
        """This is __init__ method
        Args:
          size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """this is size method
        Is to get the value of the __size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is size method
        Is to set the value of the square's size
        Args:
           value (int): Value of the new square's size
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """This is area method
        Is to calculate the area of the square
        Returns:
           The area of the square
        """
        return self.__size ** 2
