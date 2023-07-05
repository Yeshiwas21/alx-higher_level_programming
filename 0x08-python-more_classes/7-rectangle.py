#!/usr/bin/python3
"""
Amodule with a Rectangle class
"""


class Rectangle:
    """
    An empty Rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def increment():
        """
        Increments the instances
        """

        Rectangle.number_of_instances += 1

    @staticmethod
    def decrement():
        """
        Decrements the instances
        """

        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """
        Initializes some values
        Args:
        width (:obj:`int`, optional): The width of the Rectangle.
        height (:obj:`int`, optional): The height of the Rectangle.
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        self.increment()

    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            width (int): The width of the Rectangle.
        Raises:
            TypeError: If `width` type is not `int`.
            ValueError: If `width` is less than `0`.
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns the width of the Rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If `height` type is not `int`.
            ValueError: If `height` is less than `0`.
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Prints empty string
        """

        rectstr = ''
        w = self.__width
        h = self.__height

        g = str(self.print_symbol)

        if w > 0 or h > 0:
            return '{}{}'.format((g * w + '\n') * (h - 1), g * w)

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """

        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """
        section which disposes routine for del cases
        """

        self.decrement()
        print("Bye rectangle...")