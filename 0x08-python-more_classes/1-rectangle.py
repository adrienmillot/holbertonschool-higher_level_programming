#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class Rectangle that defines a rectangle """
    __height = None
    __width = None

    def __init__(self, prmWidth=0, prmHeight=0):
        self.height = prmHeight
        self.width = prmWidth

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, prmValue):
        if not isinstance(prmValue, int):
            raise TypeError("height must be an integer")
        if prmValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = prmValue

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, prmValue):
        if not isinstance(prmValue, int):
            raise TypeError("width must be an integer")
        if prmValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = prmValue
