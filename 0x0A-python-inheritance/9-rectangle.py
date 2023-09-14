#!/usr/bin/python3
"""this will define a class Rectangle that will inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this will represent a rectangle that uses BaseGeometry"""

    def __init__(self, width, height):
        """this will start a new Rectangle.

        Arguments:
            width: This is the new Rectangle's width
            height: This is the new Rectangle's height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle's area"""
        return self.__width * self.__height

    def __str__(self):
        """it should return the print() and str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
