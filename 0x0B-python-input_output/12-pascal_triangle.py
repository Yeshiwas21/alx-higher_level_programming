#!/usr/bin/python3
"""
defined module
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to a given level

    Args:
        n (int): The number of levels of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        row.append(1)
        triangle.append(row)
    return triangle
