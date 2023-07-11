#!/usr/bin/python3
"""
defined module
"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The deserialized object.
    """

    return json.loads(my_str)
