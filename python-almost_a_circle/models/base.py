#!/usr/bin/python3
"""
Base module
"""
import json


class Base:
    """ Base class of Everything """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructure """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(3, 5, 1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([x.to_dictionary() for x in list_objs]))

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats for sharing data representation.
        JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
