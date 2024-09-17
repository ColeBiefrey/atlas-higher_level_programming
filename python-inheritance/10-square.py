#!/usr/bin/python3
"""
interpolation of previous work for squares
"""

Rectangle = __import__('9-rectangle').Rectangle
"""
rectangle import and start
"""

class Square(Rectangle):
    """
    Class that defines a Square from Rectangle class
    """
    def __init__(self, size):
        """
        Method that initializes a Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Method that returns a string with the area
        """
        return super().area()
