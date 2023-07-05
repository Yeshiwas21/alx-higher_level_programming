#!/usr/bin/python3
"""
A module with a Rectangle class
"""


class Rectangle:
    """
    A class representing a rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height

        self.increment()

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self._width + self._height) if self._width != 0 and self._height != 0 else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ''
        return (str(self.print_symbol) * self._width + '\n') * (self._height - 1) + str(self.print_symbol) * self._width

    def __repr__(self):
        """
        Returns the string representation of the Rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """
        Performs the cleanup routine for the Rectangle object.
        """
        self.decrement()
        print("Bye rectangle...")

    @staticmethod
    def increment():
        """
        Increments the number of instances.
        """
        Rectangle.number_of_instances += 1

    @staticmethod
    def decrement():
        """
        Decrements the number of instances.
        """
        Rectangle.number_of_instances -= 1