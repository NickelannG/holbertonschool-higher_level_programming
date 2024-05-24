#!/usr/bin/python3
"""
task_05_dragon:
    This module contains the Mixins SwimMix and FlyMixin,
    and the Dragon class.
"""


class SwimMixin:
    """
    Mixin that contains the swim method
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that contains the fly method
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    class that inhertis both the SwimMixin and FlyMixin mixins
    """
    def roar(self):
        print("The dragon roars!")
