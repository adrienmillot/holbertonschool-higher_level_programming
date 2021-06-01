#!/usr/bin/python3
""" inherits_from module """


def inherits_from(prmObj: object, prmClassName):
    """ inherits_from function """
    return (
        type(prmObj) is not prmClassName and
        issubclass(type(prmObj), prmClassName)
    )
