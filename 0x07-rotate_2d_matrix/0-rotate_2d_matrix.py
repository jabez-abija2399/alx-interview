#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise. """
    matrix_size = len(matrix)
    for row_index in range(int(matrix_size / 2)):
        distance_from_edge = 0
        i = matrix_size - 1 - row_index

        for column_index in range(row_index, matrix_size - 1 - row_index):
            top_value = matrix[row_index][column_index]
            matrix[row_index][column_index] = matrix[i - distance_from_edge][row_index]
            matrix[i - distance_from_edge][row_index] = matrix[i][i - distance_from_edge]
            matrix[i][i - distance_from_edge] = matrix[column_index][i]
            matrix[column_index][i] = top_value
            distance_from_edge += 1
