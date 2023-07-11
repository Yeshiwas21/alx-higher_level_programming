#!/usr/bin/python3
"""
defined module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write the JSON data to.

    Returns:
        None
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
