#!/usr/bin/python3
""" save_to_json_file module """


import json


def save_to_json_file(prmObj, prmFileName):
    """
        function to save an object to a file

        Args:
            prmObj: object
            prmFileName: name of the file
    """
    with open(prmFileName, 'w') as file:
        json.dump(prmObj, file)
    file.closed
