#!/usr/bin/python3
"""this will define a class MyList inherited list """


class MyList(list):
    """this will implement a sorted printing for built-in list class"""

    def print_sorted(self):
        """this wil print a list which is in assorted ascending order"""
        print(sorted(self))
