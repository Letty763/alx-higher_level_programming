#!/usr/bin/python3
"""this will define a funtion for file-appending"""


def append_write(filename="", text=""):
    """this will append a string to the end of the UTF8 text file

    Arguments:
        filename: This is the name of the file which needs to be appended
        text: This is the string chich will be appended to the file
        
    Returns:
        The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
