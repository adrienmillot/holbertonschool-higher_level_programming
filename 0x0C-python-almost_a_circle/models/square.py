#!/usr/bin/python3
""" Square module """


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, prmSize, prmX=0, prmY=0, prmId=None):
        """
            Constructor function

            Args:
                prmWidth:  width
                prmHeight: height
                prmX:      left margin
                prmY:      top margin
                prmId:     id
        """
        super().__init__(
            prmWidth=prmSize,
            prmHeight=prmSize,
            prmX=prmX,
            prmY=prmY,
            prmId=prmId
        )

    def __str__(self):
        """
            Function that return a string representation of the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """ y getter """
        return self.width

    @size.setter
    def size(self, prmValue):
        """ size setter """
        Base.strict_integer_validation("size", prmValue)
        self.width = prmValue
        self.height = prmValue

    def update(self, *prmArgs, **prmKArgs):
        """
            Function that assigns an argument to each attribute

            Args:
                prmArgs: argument's array
                prmKArgs: argument's dictionary
        """
        if len(prmArgs) > 0:
            if len(prmArgs) > 0:
                self.strict_integer_validation("id", prmArgs[0])
                self.id = prmArgs[0]
            if len(prmArgs) > 1:
                self.width = prmArgs[1]
                self.height = prmArgs[1]
            if len(prmArgs) > 2:
                self.x = prmArgs[2]
            if len(prmArgs) > 3:
                self.y = prmArgs[3]
        else:
            if "id" in prmKArgs:
                self.strict_integer_validation("id", prmKArgs["id"])
                self.id = prmKArgs["id"]
            if "size" in prmKArgs:
                self.width = prmKArgs["size"]
                self.height = prmKArgs["size"]
            if "x" in prmKArgs:
                self.x = prmKArgs["x"]
            if "y" in prmKArgs:
                self.y = prmKArgs["y"]

    def to_dictionary(self):
        """
            Function that returns the dictionary representation of the instance
        """
        return {"x": self.x, "y": self.y, "id": self.id, "size": self.size}
