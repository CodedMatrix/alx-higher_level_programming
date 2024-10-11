#!/usr/bin/python3
"""
This module defines the print_square function.
"""

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The length of the square's sides (must be an integer).

    Raises:
        TypeError: If size is not an integer or if it is a float and less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
