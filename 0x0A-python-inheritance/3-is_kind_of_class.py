#!/usr/bin/python3
"""
A function that checks if an object is an instance of a specific class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or its subclasses.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if the object is an instance of the class or its subclasses, False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False