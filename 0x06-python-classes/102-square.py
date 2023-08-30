#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """This will start  a new square.

        Args:
            size (int): The new squares size.
        """
        self.size = size

    @property
    def size(self):
        """Sets the squares current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison to a Square."""
        return self.area() >= other.area()
