#!/usr/bin/python3

"""
    Module containing a rectangle class that
    inherits from the BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        A rectangle class.
    """
    def __init__(self, prmWidth, prmHeight):
        """
            Initialization method.

            Args:
                width: width of a rectangle.
                height: height of a rectangle.
        """
        self.integer_validator("width", prmWidth)
        self.integer_validator("height", prmHeight)
        self.__width = prmWidth
        self.__height = prmHeight
