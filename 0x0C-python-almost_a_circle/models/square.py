#!/usr/bin/python3
""" Square module """


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
        self.width = prmValue
        self.height = prmValue
