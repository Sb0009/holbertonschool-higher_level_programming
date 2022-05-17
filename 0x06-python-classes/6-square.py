#!/usr/bin/python3
"""Module to create a class
"""


class Square:
    """This is the Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """This is the __init__ method
        Is to initianilize the variables
        Args:
          size (int): size square
          position (tuple): position in x and y
        """
        self.__size = size

        if type(position) != tuple or len(position) != 2\
           or type(position[0]) != int \
           or type(position[1]) != int \
           or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @property
    def position(self):
        """this is a position method
        Is to get the position
        Returns:
           The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This is a position method
        Is to set the value of the position
        Args:
            value (tuple): position
        """
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @property
    def size(self):
        """This is a size method
        Is to get the size of the square
        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a size method
        Is to set the square's size
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
        """This is the area method
        Is to calculate the area of the square
        Returns:
           The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """This is the my_print method
        Is to print the square with #
        """
        if (self.__size == 0):
            print()

        else:
            for i in range(self.__position[1]):
                print()
        for row in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
