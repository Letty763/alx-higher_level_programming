#!/usr/bin/python3
"""this will define a BaseGeometry's base geometry class"""


class BaseGeometry:
    """this will reprsent a base geometry."""

    def area(self):
        """this area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this will prove a parameter as an integer.

        Arguments:
            name: this will be the patameters name
            value: this will be the patameter which needs to be validated
            
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
