#!/usr/bin/python3
"""
This module defines functions for file operations.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """

    with open(filename, 'a') as file:
        return file.write(text)
