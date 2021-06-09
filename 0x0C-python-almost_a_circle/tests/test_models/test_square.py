#!/usr/bin/python3


import json
from models.base import Base
from models.square import Square
import os
import unittest


class SquareTest(unittest.TestCase):
    """ SquareTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Square.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Square.__init__.__doc__), 0)

    def testSizeDocumentation(self):
        """
            Size have documentation
        """
        self.assertGreater(len(Square.size.__doc__), 0)

    def testIdInitialization(self):
        """
            Function that test object id initialization at creation
        """
        Base._Base__nb_objects = 0

        s1 = Square(10)
        self.assertEqual(s1.id, 1)

        s2 = Square(10)
        self.assertEqual(s2.id, 2)

        s3 = Square(10, 7, 9, 20)
        self.assertEqual(s3.id, 20)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.width, 10)
        self.assertEqual(s3.height, 10)

        s3.size = 57
        self.assertEqual(s3.size, 57)
        self.assertEqual(s3.width, 57)
        self.assertEqual(s3.height, 57)

        s2 = Square(5)
        self.assertEqual(s2.id, 3)

    def testIntegerValidationTypeError(self):
        """
            Function test type integer validation
        """
        with self.assertRaises(TypeError):
            s1 = Square("a", 5, 4)

        with self.assertRaises(TypeError):
            s1 = Square(2, "a", 4)

        with self.assertRaises(TypeError):
            s1 = Square(2, 5, "a")
        with self.assertRaises(TypeError):
            s1 = Square(1.2, 5, 4)

        with self.assertRaises(TypeError):
            s1 = Square(2, 2.3, 4)

        with self.assertRaises(TypeError):
            s1 = Square(2, 5, 3.4)

        try:
            r = Square("Holberton", 2, 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        try:
            r = Square(2, "Orange", 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        try:
            r = Square(2, 2, "Salad")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

        try:
            r = Square(3.7, 4, 5)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        try:
            r = Square(3, 4.3, 5)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        try:
            r = Square(3, 4, 5.6)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

    def testIntegerValidationValueError(self):
        """
            Function test value integer validation
        """
        with self.assertRaises(ValueError):
            r = Square(0)

        with self.assertRaises(ValueError):
            r = Square(-4)

        with self.assertRaises(ValueError):
            r = Square(4, -3)

        with self.assertRaises(ValueError):
            r = Square(4, 3, -2)

        with self.assertRaises(ValueError):
            r = Square(-4, -3, -2)

        try:
            r = Square(-1)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        try:
            r = Square(1, -4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        try:
            r = Square(-1, 4, 7)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        try:
            r = Square(1, -4, 7)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        try:
            r = Square(1, 4, -7)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

        try:
            r = Square(1, 4, 7, -5)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

    def testStr(self):
        """
            Function that test __str__ function
        """
        Base._Base__nb_objects = 0

        s1 = Square(3)
        self.assertEqual(s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(1, 0, 0, 3))

        s2 = Square(2)
        self.assertEqual(s2.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(2, 0, 0, 2))

        s3 = Square(8, 7, 0, 12)
        self.assertEqual(s3.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(12, 7, 0, 8))

    def testUpdate(self):
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(10, 10, 10, 10))

        s1.update(89)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 10, 10, 10))

        s1.update(89, 2)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 10, 10, 2))

        s1.update(89, 2, 3)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 3, 10, 2))

        s1.update(89, 2, 3, 4)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 3, 4, 2))

        s1.update(89, 2, 3, 4, 5)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 3, 4, 2))

        with self.assertRaises(TypeError):
            s1.update("a")

        try:
            s1.update("a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "id must be an integer")

        with self.assertRaises(ValueError):
            s1.update(-1)

        try:
            s1.update(-1)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "id must be > 0")

        with self.assertRaises(TypeError):
            s1.update(89, "a")

        try:
            s1.update(89, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        with self.assertRaises(ValueError):
            s1.update(89, -2)

        try:
            s1.update(89, -2)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        with self.assertRaises(TypeError):
            s1.update(89, 2, "a")

        try:
            s1.update(89, 2, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        with self.assertRaises(ValueError):
            s1.update(89, 2, -3)

        try:
            s1.update(89, 2, -3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        with self.assertRaises(TypeError):
            s1.update(89, 2, 3, "a")

        try:
            s1.update(89, 2, 3, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

        with self.assertRaises(ValueError):
            s1.update(89, 2, 3, -4)

        try:
            s1.update(89, 2, 3, -4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

        s1.update(height=1)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 3, 4, 2))

        s1.update(width=1, x=2)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(89, 2, 4, 2))

        s1.update(y=1, width=2, x=3, id=90)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(90, 3, 1, 2))

        s1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(90, 1, 3, 2))

        with self.assertRaises(TypeError):
            s1.update(id="a")

        try:
            s1.update(id="a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "id must be an integer")

        with self.assertRaises(ValueError):
            s1.update(id=-1)

        try:
            s1.update(id=-1)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "id must be > 0")

        with self.assertRaises(TypeError):
            s1.update(id=89, size="a")

        try:
            s1.update(id=89, size="a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        with self.assertRaises(ValueError):
            s1.update(id=89, size=-2)

        try:
            s1.update(id=89, size=-2)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        with self.assertRaises(TypeError):
            s1.update(id=89, size=2, x="a")

        try:
            s1.update(id=89, size=2, x="a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        with self.assertRaises(ValueError):
            s1.update(id=89, size=2, x=-4)

        try:
            s1.update(id=89, size=2, x=-4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        with self.assertRaises(TypeError):
            s1.update(id=89, size=2, x=4, y="a")

        try:
            s1.update(id=89, size=2, x=4, y="a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

        with self.assertRaises(ValueError):
            s1.update(id=89, size=2, height=3, x=4, y=-5)

        try:
            s1.update(id=89, size=2, x=4, y=-5)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

    def testToDictionary(self):
        """
            Function test that to_dictionary function
        """
        Base._Base__nb_objects = 0

        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(
            s1.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(9, 2, 1, 10))
        self.assertEqual(
            s1_dictionary, {'x': s1.x, 'y': s1.y, 'id': s1.id, 'size': s1.size})

        s2 = Square(1, 1)
        self.assertEqual(
            s2.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(1, 1, 0, 1))
        s2.update(**s1_dictionary)
        self.assertEqual(
            s2.__str__(), "[Square] ({:d}) {:d}/{:d} - {:d}".format(9, 2, 1, 10))

    def testSaveToFile(self):
        Base._Base__nb_objects = 0

        list = None
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(
            ), '[]')
        os.remove("Square.json")

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        list = [s1, s2]
        Square.save_to_file(list)

        with open("Square.json", "r") as file:
            reader = file.read()
            to_dict = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(reader, json.dumps(to_dict))
        os.remove("Square.json")

        list = []
        Square.save_to_file(list)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(
            ), '[]')
        os.remove("Square.json")

    def testFromJsonString(self):
        """
            Function that test json to list transformation
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertListEqual(list_output, list_input)

    def testCreate(self):
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2, "Object are not equal")
        self.assertNotEqual(s1, s2, "Values are not equal")
        self.assertNotEqual(s1_dictionary, s2.to_dictionary, "Values are not equal")

        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2, "Object are not equal")
        self.assertNotEqual(s1, s2, "Values are not equal")
        self.assertNotEqual(s1_dictionary, s2.to_dictionary, "Values are not equal")

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2, "Object are not equal")
        self.assertNotEqual(s1, s2, "Values are not equal")
        self.assertNotEqual(s1_dictionary, s2.to_dictionary, "Values are not equal")

        s1 = Square(3, 5, 1, 3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2, "Object are not equal")
        self.assertNotEqual(s1, s2, "Values are not equal")
        self.assertNotEqual(s1_dictionary, s2.to_dictionary, "Values are not equal")

    def test_load_from_file(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6)
        list_input = [s1, s2]

        Square.save_to_file(list_input)

        list_output = Square.load_from_file()

        self.assertEqual(list_input[0].to_dictionary(), list_output[0].to_dictionary())
        self.assertEqual(list_input[1].to_dictionary(), list_output[1].to_dictionary())

        os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])
