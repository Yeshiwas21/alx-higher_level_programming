#!/usr/bin/python3
"""
Amodule with a Rectangle class
"""


class Rectangle:
    """
    A class representing a rectangle.
    """

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
            raise TypeError("Width must be an integer.")
        if width < 0:
            raise ValueError("Width must be >= 0.")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")
        if height < 0:
            raise ValueError("Height must be >= 0.")
        self.__height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

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
            raise TypeError("Width must be an integer.")
        if value < 0:
            raise ValueError("Width must be >= 0.")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

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
            raise TypeError("Height must be an integer.")
        if value < 0:
            raise ValueError("Height must be >= 0.")
        self.__height = value

