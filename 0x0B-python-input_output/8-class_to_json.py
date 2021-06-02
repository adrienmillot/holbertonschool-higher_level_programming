#!/usr/bin/python3
""" class_to_json module """


def class_to_json(prmObject):
    """
        function to generate a json from an object

        Args:
            prmObject: object
    """
    return prmObject.__dict__
