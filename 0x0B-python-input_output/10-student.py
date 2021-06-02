#!/usr/bin/python3
""" student module """


class Student:
    """ Student class """

    first_name = None
    last_name = None
    age = None

    def __init__(self, prmFirstName, prmLastName, prmAge):
        """
            Constructor function

            Args:
                prmFirstName:
                prmLastName:
                prmAge:
        """
        self.first_name = prmFirstName
        self.last_name = prmLastName
        self.age = prmAge

    def to_json(self, prmAttrs=None):
        """
            Function generate a json from that class
        """
        json = {}

        if None is prmAttrs:
            return self.__dict__

        for attr in prmAttrs:
            if type(attr) is not str:
                continue
            if hasattr(self, attr):
                json[attr] = getattr(self, attr)

        return json
