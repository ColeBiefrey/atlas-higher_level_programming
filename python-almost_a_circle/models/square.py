#!/usr/bin/python3
"""
Module that contains class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes instances
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter size
        """
        self.width = value
        self.height = value
