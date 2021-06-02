#!/usr/bin/python3
""" to_json module """


import json


def to_json_string(prmObj):
    """
        function to generate a json from an object

        Args:
            prmObj: object
    """
    return json.dumps(prmObj)
