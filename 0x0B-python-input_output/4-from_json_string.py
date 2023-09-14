#!/usr/bin/python3
# 6-from_json_string.py
"""this will define the function for JSON-to-object"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
