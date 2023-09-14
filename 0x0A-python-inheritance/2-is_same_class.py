#!/usr/bin/python3
"""this will define a function which checks classes"""


def is_same_class(obj, a_class):
    """it will check if the object is an instance of a class which is given

    Arguments:
        obj: this is the object which needs to be checked
        a_class: this is the class that matches the type of object
    Returns:
        True if the object is exactly an instance of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
