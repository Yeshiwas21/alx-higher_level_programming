#!/usr/bin/python3
"""
A Square Class
"""


class Square:
    """ represents a square """
    def __init__(self, size=0):
        """__init__
        The __init__ method initializes the size of the square.
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """area returns the current area of square"""

        return self.__size * self.__size
