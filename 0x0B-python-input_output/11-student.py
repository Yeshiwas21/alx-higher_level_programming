#!/usr/bin/python3
"""
defined module
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to include in the dictionary
                          Defaults to None.

        Returns:
            dict: The dictionary representation of the student.
        """

        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance.

        Args:
            json (dict): The dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

