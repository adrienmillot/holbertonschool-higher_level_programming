#!/usr/bin/python3
""" Rectangle module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    __height = None
    __width = None
    __x = None
    __y = None

    def __init__(self, prmWidth, prmHeight, prmX=0, prmY=0, prmId=None):
        """
            Constructor

            Args:
                prmId: id
        """
        super().__init__(prmId=prmId)
        self.width = prmWidth
        self.height = prmHeight
        self.x = prmX
        self.y = prmY

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, prmValue):
        """ height setter """
        self.__height = prmValue

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, prmValue):
        """ width setter """
        self.__width = prmValue

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, prmValue):
        """ x setter """
        self.__x = prmValue

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, prmValue):
        """ y setter """
        self.__y = prmValue
