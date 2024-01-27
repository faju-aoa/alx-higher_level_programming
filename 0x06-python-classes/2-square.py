#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """representing the square class"""

    def __init__(self, size=0):
        """Initializing this square class
        Args: size - represnets the size of the square class
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
