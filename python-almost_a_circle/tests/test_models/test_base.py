#!/usr/bin/python3
"""Test Base model"""
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """test cases for Base"""
    def test_id(self):
        self.assertEqual(Base(42).id, 42)

    def test_id_next(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_string(self):
        self.assertEqual(Base("fffff").id, "fffff")

    def test_id_none(self):
        self.assertEqual(Base(None).id, 3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{"id": 5}]), '[{"id": 5}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"id": 15}]'), [{"id": 15}])


if __name__ == "__main__":
    unittest.main()
