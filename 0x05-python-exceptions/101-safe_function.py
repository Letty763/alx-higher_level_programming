#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: this is the function that needs to be executed.
        args: this is the arguments for the function.

    Returns:
        Returns the results of the function,
        Otherwise,it returns Nothing if something happens during the function and prints in stderr the error precede by Exception:
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
