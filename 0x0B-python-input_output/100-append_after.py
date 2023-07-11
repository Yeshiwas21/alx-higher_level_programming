#!/usr/bin/python3
"""
defined module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends the new_string after each occurrence of the search_string

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for.
        new_string (str): The string to append after each occurrence.

    Returns:
        None
    """

    with open(filename, "r") as file:
        text = file.readlines()

    with open(filename, "w") as file:
        updated_text = ""
        for line in text:
            updated_text += line
            if search_string in line:
                updated_text += new_string
        file.write(updated_text)
