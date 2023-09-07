!/usr/bin/python3
""" Define a locked class"""


class LockedClass:
    """
    allows instatiation of an attribute  first_name only
    """

    __slots__ = ["first_name"]
