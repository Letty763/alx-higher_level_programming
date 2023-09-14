#!/usr/bin/python3
"""this will define a inherited function which checks classes"""


def inherits_from(obj, a_class):
    """it will check if an object is actually an inherited instance of a class

    Arguments:
        obj: this is the object which needs to be checked
        a_class: this is the class which needs to match the object which is checked
        
    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
