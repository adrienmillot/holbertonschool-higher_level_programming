#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ MyInt class """

    def __eq__(self, prmObject):
        """ equals function """
        return super() == prmObject

    def __ne__(self, prmObject):
        """ not equals function """
        return not self.__eq__(prmObject)
