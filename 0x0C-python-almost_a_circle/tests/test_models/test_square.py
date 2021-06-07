#!/usr/bin/python3


from models.base import Base
from models.square import Square
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
            r = Square(-4, -3, -2)

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
