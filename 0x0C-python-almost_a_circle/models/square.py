#!/usr/bin/python3
"""Defines a square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """User-friendly representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        The method assigns the provided arguments or keyword arguments to the 
        corresponding attributes of the `Square` object.
        The attributes that can be updated include 'id', 'size', 'x', and 'y'.

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
                self.size = args[1]
            if num_args > 2:
                self.x = args[2]
            if num_args > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        dict = {'id': self.id, 'size': self.size,
                               'x': self.x, 'y': self.y}
        return (dict)
