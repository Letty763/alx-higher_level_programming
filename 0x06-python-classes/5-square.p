#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """This initializes the new square.

        Args:
            size (int): the  brand new squares size.
        """
        self.size = size

    @property
    def size(self):
        """current size of the square is set."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """brings back the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """will print the square with # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
