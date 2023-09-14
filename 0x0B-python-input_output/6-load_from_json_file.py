#!/usr/bin/python3
"""this will define the function for the JSON file-reading"""
import json


def load_from_json_file(filename):
    """this will then create a Python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
