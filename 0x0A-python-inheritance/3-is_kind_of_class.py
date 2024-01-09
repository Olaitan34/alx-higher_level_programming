#!/usr/bin/python3
"""Function that retrns true or false"""


def is_kind_of_class(obj, a_class):
    """"Checks if the object is an instance of, 
    or if the object is an instance of a class 
    that inherited from, the specified class

    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.
    Returns:
    If obj is exactly an instance of a_class - True.
    Otherwise - False."""
    if isinstance(obj, a_class):
        return True
    else:
       return False
