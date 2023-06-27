#!/usr/bin/python3
"""
a square class
"""


class Square:
    """represents a square"""

    def __init__(self, size=0):

        """__init__
        this function Instantiate with size attribute with
        positive integers
        Attributes:
        size
        Raises:
        TypeError and ValueError"""
        self.size = size

    @property
    def size(self):

        """ value getter"""

        return (self.__size)

    @size.setter
    def size(self, value):

        """value setter"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):

        """this method returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):

        """prints a square using #"""

        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.size):
                    print('#', end='')
                print()
