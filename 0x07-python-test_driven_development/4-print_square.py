#!/usr/bin/python3
""" print_square module """


def print_square(prmSize):
    """ print_square function

    this function print a square

    Attributes:
        prmSize: square size
    """
    if not isinstance(prmSize, int) or isinstance(prmSize, float):
        raise TypeError("size must be an integer")
    elif prmSize < 0:
        raise ValueError("size must be >= 0")
    for y in range(prmSize):
        [print("#", end='') for x in range(prmSize)]
        print()
    if prmSize == 0:
        print()
