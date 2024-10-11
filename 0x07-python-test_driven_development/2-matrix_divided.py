#!/usr/bin/python3
"""
This module defines the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor, rounded to 2 decimal places.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (must be an integer or float).

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, or if rows are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are integers or floats and rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return a new matrix with elements divided by div
    return [[round(num / div, 2) for num in row] for row in matrix]
