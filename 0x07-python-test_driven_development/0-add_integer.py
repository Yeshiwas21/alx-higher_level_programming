#!/usr/bin/python3
"""
A function that adds two integers. By default, b is 98
"""


def add_integer(a, b=98):
    """Our function to add two integers: a and b

    Args:
        a (int): The first parameter
        b (int): The second parameter

    Returns:
        int: The sum of the parameters
        exception: In case there is one or more

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
