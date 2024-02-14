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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats for sharing data representation.
        JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
