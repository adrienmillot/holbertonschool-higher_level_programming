#!/usr/bin/python3
""" Base module """


class Base:
    """ Base class """
    __nb_objects = 0
    id = 0

    def __init__(self, prmId=None):
        """
            Constructor

            Args:
                prmId: id
        """
        if None is not prmId:
            self.id = prmId
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def strict_integer_validation(prmName, prmValue):
        """
            strict integer validation

            Args:
                prmName: name of the variable
                prmValue: value of the variable
        """
        if type(prmValue) is not int:
            raise TypeError("{} must be an integer".format(prmName))
        if prmValue <= 0:
            raise ValueError("{} must be > 0".format(prmName))

    @staticmethod
    def integer_validation(prmName, prmValue):
        """
            variable integer validation

            Args:
                prmName: name of the variable
                prmValue: value of the variable
        """
        if type(prmValue) is not int:
            raise TypeError("{} must be an integer".format(prmName))
        if prmValue < 0:
            raise ValueError("{} must be >= 0".format(prmName))
