#!/usr/bin/python3
"""this will define a function for file-writing"""


def write_file(filename="", text=""):
    """this will write a string to the UTF8 text file.

    Arguments:
        filename: This is the name of the file which needs to be written
        text: This is the text which needs to be written to the file
        
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
