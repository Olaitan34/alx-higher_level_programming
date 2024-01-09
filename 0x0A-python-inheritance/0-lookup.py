#!/usr/bin/python3
"""Function that list the Attributes and method in a class"""


def lookup(obj):
    """Returns the list of Available Attributes"""
    return dir(obj)
