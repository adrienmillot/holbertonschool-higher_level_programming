#!/usr/bin/python3
""" RectangleTest module """


from models.base import Base
from models.rectangle import Rectangle
from tests.test_models.tools import Tools
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
            r = Rectangle(-1, 4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")

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

    def testArea(self):
        """
            Function that test area function
        """

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6, "area() doesn't return good value")

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20, "area() doesn't return good value")

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56, "area() doesn't return good value")

        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def testDisplay(self):
        """
            Function that test display function
        """
        r = Rectangle(2, 3, 0, 0, 0)
        capture = Tools.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

        r = Rectangle(3, 2, 1, 0, 1)
        capture = Tools.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

        r = Rectangle(4, 5, 0, 1, 0)
        capture = Tools.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

        r = Rectangle(2, 4, 3, 2, 0)
        capture = Tools.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

    def testStr(self):
        """
            Function that test __str__ function
        """
        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(1, 0, 0, 3, 2), "wrong return")

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(2, 0, 0, 2, 10), "wrong return")

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(12, 0, 0, 8, 7), "wrong return")

    def testUpdate(self):
        """
            Function that test update function
        """
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(1, 10, 10, 10, 10), "wrong string return")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(89, 10, 10, 10, 10), "wrong string return")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(89, 10, 10, 2, 10), "wrong string return")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(89, 10, 10, 2, 3), "wrong string return")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(89, 4, 10, 2, 3), "wrong string return")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(89, 4, 5, 2, 3), "wrong string return")

        with self.assertRaises(TypeError):
            r1.update("a")

        try:
            r1.update("a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "id must be an integer", "wrong message")

        with self.assertRaises(ValueError):
            r1.update(-1)

        try:
            r1.update(-1)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "id must be > 0", "wrong message")

        with self.assertRaises(TypeError):
            r1.update(89, "a")

        with self.assertRaises(TypeError):
            r1.update(89, 1.0)

        try:
            r1.update(89, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer", "wrong message")

        with self.assertRaises(ValueError):
            r1.update(89, -2)

        try:
            r1.update(89, -2)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0", "wrong message")

        with self.assertRaises(TypeError):
            r1.update(89, 2, "a")

        with self.assertRaises(TypeError):
            r1.update(89, 2, 1.0)

        try:
            r1.update(89, 2, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "height must be an integer", "wrong message")

        with self.assertRaises(ValueError):
            r1.update(89, 2, -3)

        try:
            r1.update(89, 2, -3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "height must be > 0", "wrong message")

        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, "a", "x shouldn't be a string")

        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, 1.0, "x shouldn't be a float")

        try:
            r1.update(89, 2, 3, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer", "wrong message")

        with self.assertRaises(ValueError):
            r1.update(89, 2, 3, -4)

        try:
            r1.update(89, 2, 3, -4)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0", "wrong message")

        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, 4, "a", "y shouldn't be a string")

        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, 4, 1.0, "y shouldn't be a float")

        try:
            r1.update(89, 2, 3, 4, "a")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer", "wrong message")

        with self.assertRaises(ValueError):
            r1.update(89, 2, 3, 4, -5)

        try:
            r1.update(89, 2, 3, 4, -5)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0", "wrong message")
