#!/usr/bin/python3
"""This modle is influenced by the list"""


class MyList(list):
    """The class that returns the list"""
    def  print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
