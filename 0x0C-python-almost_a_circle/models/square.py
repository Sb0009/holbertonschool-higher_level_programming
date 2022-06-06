#!/usr/bin/python3
"""Module to create a square
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Error
        documentation
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Error
        documentation
        """

        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Error
        documentation
        """

        self.heigth = value
        self.width = value

    def update(self, *args, **kwargs):
        """Error
        documentation
        """

        if args is None or len(args) == 0:
            for item in kwargs:
                if hasattr(self, item):
                    if item == 'id':
                        self.id = kwargs[item]
                    if item == 'size':
                        self.width = kwargs[item]
                        self.height = kwargs[item]
                    if item == 'x':
                        self.x = kwargs[item]
                    if item == 'y':
                        self.y = kwargs[item]
        else:
            len_args = len(args)

            if (len_args > 0):
                self.id = args[0]

            if (len_args > 1):
                self.width = args[1]
                self.width = args[1]

            if (len_args > 2):
                self.x = args[2]

            if (len_args > 3):
                self.y = args[3]

    def to_dictionary(self):
        """Error
        documentation
        """

        return {'id': self.id, 'size': self._Rectangle__width,
                'x': self._Rectangle__x,
                'y': self._Rectangle__y}

    def __str__(self):
        """Error
        documentation
        """

        msg = '[Square] ({:d}) {:d}/{:d} - {:d}'
        return msg.format(self.id, self._Rectangle__x, self._Rectangle__y,
                          self._Rectangle__width)
