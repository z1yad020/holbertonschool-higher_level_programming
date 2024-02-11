#!/usr/bin/python3


"""Module"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def reload_from_json(self, json):
        if not json:
            return
    self.first_name = json["first_name"]
    self.last_name = json["last_name"]
    self.age = json["age"]

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        result = {}

        for attr in attrs:
            if arrt in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
