#!/usr/bin/python3
"""
defined module
"""


def read_file(filename=""):
    """
    reads text file
    """

    with open(filename) as file:
        print(file.read(), end='')
