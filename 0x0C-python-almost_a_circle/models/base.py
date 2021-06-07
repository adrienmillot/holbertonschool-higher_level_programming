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
