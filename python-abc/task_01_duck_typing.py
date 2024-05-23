#!/usr/bin/python3
"""
task_01_duck_typing:
    This module contains an abstact class Shape
    with an abstract methods area and perimeter
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Absract class shape that defines a shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Subclass that inherits from the Shape class
    """
    def __init__(self, radius):
        if radius < 0:
            raise ValueError(" radius must be >= 0")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Subclass that inherits from the Shape class
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
