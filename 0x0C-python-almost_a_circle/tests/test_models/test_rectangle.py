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
        r6 = Rectangle("Holberton", "Orange")
        r7 = Rectangle(-4, -3, -2, -1, 0)
        r8 = Rectangle(3.7, 4.3, 5.6, 2.9, 7.8)

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
        self.assertEqual(r6.id, 5)
        self.assertEqual(r6.width, "Holberton")
        self.assertEqual(r6.height, "Orange")
        self.assertEqual(r6.x, 0)
        self.assertEqual(r6.y, 0)
        self.assertEqual(r7.id, 0)
        self.assertEqual(r7.width, -4)
        self.assertEqual(r7.height, -3)
        self.assertEqual(r7.x, -2)
        self.assertEqual(r7.y, -1)
        self.assertEqual(r8.id, 7.8)
        self.assertEqual(r8.width, 3.7)
        self.assertEqual(r8.height, 4.3)
        self.assertEqual(r8.x, 5.6)
        self.assertEqual(r8.y, 2.9)
