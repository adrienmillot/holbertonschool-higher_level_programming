#!/usr/bin/python3
""" BaseGeometry module """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, prmName, prmValue):
        """ integer_validator function """
        if type(prmValue) is not int:
            raise TypeError("{} must be an integer".format(prmName))
        if prmValue <= 0:
            raise ValueError("{} must be greater than 0".format(prmName))
