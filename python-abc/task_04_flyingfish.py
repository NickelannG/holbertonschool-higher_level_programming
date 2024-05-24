#!/usr/bin/python3
"""
task_04_flyingfish:
    This module contains the classes Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Defines a fish with swim and habitat methods
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Defines a birds with fly and habitat methods
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Inherits from Fish and Bird classes.

    Defines a Flying fish by overriding the fly, swim, and habitat methods
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
