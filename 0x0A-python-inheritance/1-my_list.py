#!/usr/bin/python3
"""
A class that inherits from the list data type.
"""


class MyList(list):
    """
    The main class.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """

        print(sorted(self))
