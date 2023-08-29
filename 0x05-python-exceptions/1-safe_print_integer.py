#!/usr/bin/python3


def safe_print_integer(value)7:
    """prints the integer with "{:d}".format().

    Args:
        value (int): the number that needs to be printed.

    Returns:
        Returns True when value has been correctly printed.
        Otherwise, it will return False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
