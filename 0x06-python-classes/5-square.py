#!/usr/bin/python3
"""class Square"""


class Square:
    """Size validation"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
