#!/usr/bin/python3
"""this will define the function for the text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """this will insert text after each line that has a given string in a file

    Arguments:
        filename: This will be the files name
        search_string: This will be the string which needs to be looked for in the file
        new_string: This will be the string which needs to be inserted
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
