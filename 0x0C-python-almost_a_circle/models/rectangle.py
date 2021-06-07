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
        Base.strict_integer_validation("height", prmValue)
        self.__height = prmValue

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, prmValue):
        """ width setter """
        Base.strict_integer_validation("width", prmValue)
        self.__width = prmValue

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, prmValue):
        """ x setter """
        Base.integer_validation("x", prmValue)
        self.__x = prmValue

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, prmValue):
        """ y setter """
        Base.integer_validation("y", prmValue)
        self.__y = prmValue

    def area(self):
        """
            Function that return area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """
            Function that print in stdout the instance with the character
            # by taking care of x and y
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
            Function that return a string representation of the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

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
            if len(prmArgs) > 2:
                self.height = prmArgs[2]
            if len(prmArgs) > 3:
                self.x = prmArgs[3]
            if len(prmArgs) > 4:
                self.y = prmArgs[4]
        else:
            if "id" in prmKArgs:
                self.strict_integer_validation("id", prmKArgs["id"])
                self.id = prmKArgs["id"]
            if "width" in prmKArgs:
                self.width = prmKArgs["width"]
            if "height" in prmKArgs:
                self.height = prmKArgs["height"]
            if "x" in prmKArgs:
                self.x = prmKArgs["x"]
            if "y" in prmKArgs:
                self.y = prmKArgs["y"]

    def to_dictionary(self):
        """
            Function that returns the dictionary representation of the instance
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
