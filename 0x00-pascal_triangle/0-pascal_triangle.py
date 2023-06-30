#!/usr/bin/python3

"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Print Pascal's Triangle

    Args:
        n (int): Size of the pascal triangle
    """
    Triangle = []
    if (n <= 0):
        return Triangle
    else:
        for x in range(n+1):
            row = []
            # first element is always 1
            c = 1
            for y in range(1, x+1):
                # first value in a line is always 1
                row.append(c)
                # using Binomial Coefficient
                c = c * (x - y) // y
            if (len(row)):
                Triangle.append(temp)
    return Triangle