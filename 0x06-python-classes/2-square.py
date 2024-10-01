#!/usr/bin/python3
"""
This module defines a class `Square`.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is greater than or equal to 0
        if size < 0:
            raise ValueError("size must be >= 0")

        # Private attribute to store the size of the square
        self.__size = size

