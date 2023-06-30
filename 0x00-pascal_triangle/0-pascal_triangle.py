#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    if n == 1:
        return triangle

    for row in range(1, n):
        left = -1
        right = 0
        listInt = []
        for column in range(row+1):
            integer = 0
            if left > -1:triangle
                integer += triangle[row - 1][left]
            if right < row:
                integer += triangle[row - 1][right]
            left += 1
            right += 1
            listInt.append(integer)
        triangle.append(listInt)
    return triangle
