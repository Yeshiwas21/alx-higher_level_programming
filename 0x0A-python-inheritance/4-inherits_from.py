#!/usr/bin/python3
"""
A function that checks if an object is an instance of a specific class.
"""


def inherits_from(obj, a_class):
    """
    Checks if `obj` is an instance of a class that inherited from `a_class`.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if `obj` is an instance of a class that inherited from `a_class`,
        False otherwise.
    """

    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return (True)
    return (False)