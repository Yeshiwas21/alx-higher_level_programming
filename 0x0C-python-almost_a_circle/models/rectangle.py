#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identity of the rectangle.

        Raises:
            TypeError: If width or height is not an int.
            ValueError: If width or height is less than or equal to 0.
            TypeError: If x or y is not an int.
            ValueError: If x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get or set the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get or set the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get or set the x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get or set the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (int).
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle using the '#' character.

        Returns:
            None
        """
        print('\n' * self.__y, end="")
        for j in range(self.__height):
            print(' ' * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the `Rectangle` instance.

        Returns:
            A string representing the `Rectangle` instance.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the `Rectangle` instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        num_args = len(args)
        if num_args > 0:
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.__width = args[1]
            if num_args > 2:
                self.__height = args[2]
            if num_args > 3:
                self.__x = args[3]
            if num_args > 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
            """
            Return a dictionary representation of the rectangle.

            The method returns a dictionary with the attributes 
            of the `Rectangle` object. The dictionary includes the keys 
            'id', 'width', 'height', 'x', and 'y', mapping
            to their corresponding attribute values.

            Returns:
                A dictionary representing the `Rectangle` object.
            """
            return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
