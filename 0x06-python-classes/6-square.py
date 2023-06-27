#!/usr/bin/python3
""" This is the square class. """


class Square:
    """ This is the square class. """
    def __init__(self, size=0, position=(0, 0)):
        """ init is called to create an object. self refers to itself
        Attributes:
            size (int): This is the size of the square.
            position (int, int): These are the coordinates of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[0], int) is False or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[1], int) is False or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """ This retrieves the size"""
        return self.__size

    @property
    def position(self):
        """ This will retrieve the position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """ This sets the size of the square.
        Attributes:
            value (int): This is the value size of the square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")

        self.__size = value

    @position.setter
    def position(self, value):
        if isinstance(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[0], int) is False or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[1], int) is False or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ This will give us the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """ Prints in stdout"""

        if self.__size == 0:
            print()
        else:
            i = self.position[0] + self.size
            s = self.position[0]
            d = self.position[1]
            for j in range(d):
                print()
            for k in range(self.size):
                for m in range(i):
                    if m < s:
                        print("{}".format(" "), end="")
                    else:
                        print("{}".format("#"), end="")
                print()
