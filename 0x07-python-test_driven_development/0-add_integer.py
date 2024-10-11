#!/usr/bin/python3
"""
This module defines the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum as an integer.
    
    Args:
        a: The first integer or float.
        b: The second integer or float (defaults to 98).
    
    Returns:
        The sum of a and b, casted to integers.
    
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
