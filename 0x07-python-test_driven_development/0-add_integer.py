#!/usr/bin/python3
""" add_integer module """


def add_integer(prmA, prmB=98):
    """ add_integer function

    this function add two integer

    Attributes:
        prmA: first integer
        prmB: optional second integer (init by 98 by default)
    """
    if isinstance(prmA, float):
        prmA = int(prmA)
    if isinstance(prmB, float):
        prmB = int(prmB)
    if not isinstance(prmA, int):
        raise TypeError("a must be an integer")
    if not isinstance(prmB, int):
        raise TypeError("b must be an integer")
    return prmA + prmB
