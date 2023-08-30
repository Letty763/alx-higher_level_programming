#!/usr/bin/python3
"""This will define a MagicClass matching a bytecode given by Holberton."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """This will start a MagicClass.

        Arg:
            radius (float or int): The new  radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the current MagicClass area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns current MagicClass circumference"""
        return (2 * math.pi * self.__radius)
MagicClass
