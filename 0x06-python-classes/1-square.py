#!/usr/bin/python3

"""Defining a class Square."""


class Square:
    """
    It represents a square and can be used as a template
    for creating square objects.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.
        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
