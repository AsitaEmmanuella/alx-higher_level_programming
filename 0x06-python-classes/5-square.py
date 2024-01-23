#!/usr/bin/python3
"""Square class defining"""


class Square:
    """
    This is the Square class.
    It represents a square and can be used as a template
    for creating square objects.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the current size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Parameters:
            value (int): The size to set.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.
        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square using the character '#'.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
