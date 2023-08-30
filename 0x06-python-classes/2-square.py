#!/usr/bin/python3
"""statesa class Square."""


class Square:
    """represents the square."""

    def __init__(self, size=0):
        """this will initialize a new Square.

        Args:
            size (int): this will represent the new squares size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
