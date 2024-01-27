#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """representing the square class"""

    def __init__(self, size=0):
        """Initializing this square class
        Args: size - represnets the size of the square class
        Raises: TypeError: if size is not integer
        ValueError: if size is less than zero"""
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area of a circle method"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()
