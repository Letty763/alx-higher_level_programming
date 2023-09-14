#!/usr/bin/python3
"""this will define a function for text file-reading function"""


def read_file(filename=""):
    """this will print the contents in the UTF8 text file to standardoutput"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
