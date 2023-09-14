#!/usr/bin/python3
"""this will define a inherited class-checking function and a class"""


def is_kind_of_class(obj, a_class):
    """this will scan to see if an object is an inherited instance of a class or if it is an instance

    Arguments:
        obj: this is the object which needs to be checked
        a_class: this is the class which needs to match the object which is checked
    Returns:
        True if the object is an instance of, or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
