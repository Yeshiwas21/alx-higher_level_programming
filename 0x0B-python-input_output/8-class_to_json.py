#!/usr/bin/python3
"""
defined module
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: The object to be serialized to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """

    return obj.__dict__
