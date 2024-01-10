#!/usr/bin/python3
"""Function that converts pyon to json file"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
