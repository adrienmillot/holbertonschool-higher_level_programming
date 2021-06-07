#!/usr/bin/python3
""" RectangleTest module """


from models.base import Base
from models.rectangle import Rectangle
import unittest


class RectangleTest(unittest.TestCase):
    """ RectangleTest class """

    def testClassDocumentation(self):
        """
            Class have documentation
        """
        self.assertGreater(len(Rectangle.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor have documentation
        """
        self.assertGreater(len(Rectangle.__init__.__doc__), 0)

    def testInitId(self):
        """
            Function that test object id initialization at creation
        """
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 9, 3)
        r4 = Rectangle(10, 2, 3, 9)
        r5 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r3.x, 9)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r4.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 9)
        self.assertEqual(r5.id, 12)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def testIntegerValidationTypeError(self):
        """
            Function test type integer validation
        """
        with self.assertRaises(TypeError):
            r = Rectangle("Holberton", 2)

        with self.assertRaises(TypeError):
            r = Rectangle(2, "Orange")

        with self.assertRaises(TypeError):
            r = Rectangle(3.7, 4.3, 5.6, 2.9, 7.8)

        with self.assertRaises(TypeError):
            r = Rectangle(3.7, 4, 5, 2, 7)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 4.3, 5, 2, 7)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 5.6, 2, 7)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 5, 2.9, 7)

        try:
            r = Rectangle("Holberton", 2)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        try:
            r = Rectangle(2, "Orange")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "height must be an integer")

        try:
            r = Rectangle(3.7, 4.3, 5.6, 2.9, 7.8)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        try:
            r = Rectangle(3.7, 4, 5, 2, 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        try:
            r = Rectangle(3, 4.3, 5, 2, 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "height must be an integer")

        try:
            r = Rectangle(3, 4, 5.6, 2, 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        try:
            r = Rectangle(3, 4, 5, 2.9, 7)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

    def testIntegerValidationValueError(self):
        """
            Function test value integer validation
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-4, -3, -2, -1, 0)

        try:
            r = Rectangle(0, 4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        try:
            r = Rectangle(-1, 4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

        try:
            r = Rectangle(1, 0)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "height must be > 0")

        try:
            r = Rectangle(1, -4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "height must be > 0")

        try:
            r = Rectangle(1, 4, -7)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        try:
            r = Rectangle(1, 4, 7, -5)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")
