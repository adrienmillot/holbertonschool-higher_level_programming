#!/usr/bin/python3
""" load_from_json_file module """


import json


def load_from_json_file(prmFileName):
    """
        function load json from a file

        Args:
            prmFileName: name of the file
    """
    obj = None
    with open(prmFileName) as file:
        obj = json.load(file)
    file.closed
    return obj
