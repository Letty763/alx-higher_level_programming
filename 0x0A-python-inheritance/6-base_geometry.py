#!/usr/bin/python3
"""this eill define a BaseGeometry's base geometry class"""


class BaseGeometry:
    """this will represent base geometry"""

    def area(self):
        """area which is not implemented."""
        raise Exception("area() is not implemented")
