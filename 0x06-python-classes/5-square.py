#!/usr/bin/python3
class Square:
    """
    Represents a square shape and
    provides methods to manipulate and retrieve its size.

    Attributes:
        __size (int): Represents the size of the square.

    Methods:
        __init__: Initializes a new Square object with a specified size.
        size: Property to get/set the current size of the square.
        area: Calculates and returns the area of the square.
        my_print: Prints a square pattern
        using "#" symbols based on the square's size.
    """

    def __init__(self, size):
        """Initializes a new Square object with a specified size."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating the input."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square pattern using "#" symbols based on the square's size.
        If the size is 0, prints an empty line to indicate an empty square.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
