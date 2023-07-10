#!/usr/bin/python3
"""
defined inherits_from function
"""


def inherits_from(obj, a_class):
    """
    checks instance of a class that inherited from the specific class

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