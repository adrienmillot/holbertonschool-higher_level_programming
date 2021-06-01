#!/usr/bin/python3
""" Rectangle class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that defines a rectangle """

    def __init__(self, width, height):
        """ Constructor function """
        self.integer_validator('height', height)
        self.integer_validator('width', width)

        self.__height = height
        self.__width = width

    def area(self):
        """ Area function """
        return self.__width * self.__height

    def __str__(self):
        """ string function """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
