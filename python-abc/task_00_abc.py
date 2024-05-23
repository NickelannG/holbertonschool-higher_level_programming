#!/usr/bin/python3
"""
task_00_abc:
    This module contains an absract class Animal with an abstract method
    sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class to define an animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass that inherits from Animal class:
    Defines a dog.
    """
    def sound(self):
        return str("Bark")


class Cat(Animal):
    """
    Subclass that inhertis from Animal class:
    Defines a cat.
    """
    def sound(self):
        return str("Meow")
