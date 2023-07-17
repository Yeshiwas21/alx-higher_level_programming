#!/usr/bin/python3
"""
defined module
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The deserialized object.
    """

    with open(filename, 'r') as file:
        return json.load(file)
