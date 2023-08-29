#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """prints an integer.

    Args:
        value (int): this will be the integer which needs to be printed.

    Returns:
        True if value has ev5er been correctly printed (it means the value is an integer)
        Otherwise,will returns False and prints in stderr the error precede by Exception:
        
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
