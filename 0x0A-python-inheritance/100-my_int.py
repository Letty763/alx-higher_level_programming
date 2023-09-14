#!/usr/bin/python3
"""this will define a class MyInt which will inherit from int"""


class MyInt(int):
    """this will invert the int operators == and !="""

    def __eq__(self, value):
        """this will override the == opeartor with != behaviour"""
        return self.real != value

    def __ne__(self, value):
        """this will override the != operator with the == behaviour"""
        return self.real == value
