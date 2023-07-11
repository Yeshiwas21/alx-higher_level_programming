#!/usr/bin/python3
"""
String to a file and return the number of written characters.
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a text file.
    """

    with open(filename, 'w') as file:
        return file.write(text)
