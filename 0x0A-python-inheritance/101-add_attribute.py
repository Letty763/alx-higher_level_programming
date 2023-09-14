#!/usr/bin/python3
"""this will define a function that will add attributes to objects"""


def add_attribute(obj, att, value):
    """this will add new attributse to an object if it possible

    Arguments:
        obj: This will be the object to add an attribute to
        att: This will be the attributes name
        value): This will be the value of the attribute
        
    Raises:
        TypeError: If the attribute cannot be added to the object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
