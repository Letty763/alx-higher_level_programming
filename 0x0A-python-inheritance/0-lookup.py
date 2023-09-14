#!/usr/bin/python3
"""this will define the lookup function of an object attribute"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return (dir(obj))
