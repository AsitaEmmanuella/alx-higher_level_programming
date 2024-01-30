#!/usr/bin/python3

"""
    Adds two integers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.
    """


def add_integer(a, b=98):
    """
    Returns:
        int: The sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
