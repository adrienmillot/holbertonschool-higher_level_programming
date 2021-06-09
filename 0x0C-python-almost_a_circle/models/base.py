#!/usr/bin/python3
""" Base module """


import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Function that return  the JSON string representation
            of a dictionary
        """
        if None is list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, prmObjects):
        """
            Function that writes the JSON string representation
            of object list in a file
        """
        fileName = "{}.json".format(cls.__name__)
        list = []

        if prmObjects is None or len(prmObjects) == 0:
            prmObjects = []

        with open(fileName, 'w', encoding="UTF-8") as file:
            for elem in prmObjects:
                list.append(elem.to_dictionary())
            file.write(Base.to_json_string(list))
        file.closed

    def from_json_string(json_string):
        """
            Function that returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Function that returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            obj = cls(1, 1)
        elif cls == Square:
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
            Function returns a list of instances
        """
        fileName = "{}.json".format(cls.__name__)
        if os.path.isfile(fileName):
            with open(fileName, "r") as file:
                list_output = cls.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_output]

        return []
