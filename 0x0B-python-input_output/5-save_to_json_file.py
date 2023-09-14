#!/usr/bin/python3
"""this will define the function for JSON file-writing"""
import json


def save_to_json_file(my_obj, filename):
    """this will write an object using JSON representation to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
