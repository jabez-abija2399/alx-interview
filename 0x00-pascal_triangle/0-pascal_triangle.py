#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0.

    triangle = []  # Initialize an empty list to store the Pascal's triangle.
    for i in range(n):  # Iterate from 0 to n-1 to generate each row of the triangle.
        row = [1]  # Start each row with 1, as the first and last elements are always 1.
        if i > 0:  # Skip the following steps for the first row (i.e., when i = 0).
            prev_row = triangle[i-1]  # Get the previous row from the triangle.
            for j in range(1, i):  # Iterate from 1 to i-1 to calculate the elements in the current row.
                element = prev_row[j-1] + prev_row[j]  # Calculate the element as the sum of two elements from the previous row.
                row.append(element)  # Append the calculated element to the current row.
            row.append(1)  # End each row with 1, as the last element is always 1.

        triangle.append(row)  # Append the current row to the triangle.

    return triangle  # Return the generated Pascal's triangle.

