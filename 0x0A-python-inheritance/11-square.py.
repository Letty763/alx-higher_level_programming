#!/usr/bin/python3
"""this will define the subclass Square of a Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this will represent a Square"""

    def __init__(self, size):
        """this will start a new Square

        Arguments:
            size: This is thenew square's size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
