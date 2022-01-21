#!/usr/bin/python3
"""class Square"""


class Square:
    """Size validation"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size * self.__size
