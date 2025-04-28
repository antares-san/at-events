"""
My animal class

"""

from abc import ABC, abstractmethod
import json


class Animal(ABC):

    def __init__(self, file_name):
        """

        file_name:
        """

        # private members
        self.__data = self.__read_file(file_name)
        self.__group_name = self.__data["group_name"]
        self.__animal_type = self.__data["animal_type"]

    # A private method
    @staticmethod
    def __read_file(file_name):
        """

        file_name:
        :param file_name:
        :return:
        """
        with open(file_name, "r") as file:
            data = json.load(file)
        return data

    @property
    def data(self):
        return self.__data

    @property
    def group_name(self):
        return self.__group_name

    @property
    def animal_type(self):
        return self.__animal_type

    # An abstract method
    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return "Unknown animal"

