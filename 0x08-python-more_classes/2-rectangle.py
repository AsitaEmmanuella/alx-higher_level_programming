#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class with private width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialization method with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets method for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets method for height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
