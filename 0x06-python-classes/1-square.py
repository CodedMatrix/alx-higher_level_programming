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

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square (no type/value validation).
        
        The size attribute is private because its control is crucial for calculations 
        such as the area, and it should not be accessed or modified directly from outside the class.
        """
        # Private attribute to store the size of the square
        self.__size = size

