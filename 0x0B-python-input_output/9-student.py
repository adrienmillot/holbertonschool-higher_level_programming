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

    def to_json(self):
        """
            Function generate a json from that class
        """
        return self.__dict__
