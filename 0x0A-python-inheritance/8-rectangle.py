#!/usr/bin/python3
"""this will define a Rectangle class which will inherit from the BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this will represent a rectangle which uses BaseGeometry"""

    def __init__(self, width, height):
        """this will start a new Rectangle.

        Arguments:
            width: this will be the new Rectangle's width
            height: this will be thenew Rectangle's height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
