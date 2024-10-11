#!/usr/bin/python3
"""
This module defines the text_indentation function.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text: The text to be printed (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a variable to accumulate the output
    output = ""
    for char in text:
        output += char
        if char in '.?:':
            output += "\n\n"

    # Remove leading/trailing whitespace and print
    print("\n".join(line.strip() for line in output.splitlines()))
