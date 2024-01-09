#!/usr/bin/python3
"""Checks if class was inheritd directly or indirectly"""


def inherits_from(obj, a_class):
    """Checks whether or not a class was inherited directly or indirectly

    Args:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.
    Return:
    True if inherited directly and false if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False 
