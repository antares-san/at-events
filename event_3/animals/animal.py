"""
My animal class

"""

from abc import ABC, abstractmethod
import json


class Animal(ABC):

    # static variables of Animal class
    counter = 0 

    def __init__(self, group_name):
        """

        """

        # private members
        self.__group_name = group_name
        
        # static variable
        Animal.counter += 1

    # A public method
    @staticmethod
    def getCounter():
        return Animal.counter

    @property
    def group_name(self):
        return self.__group_name

    # An abstract method
    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return "Unknown animal"

