#!/usr/bin/python3
"""Test Base model"""
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """test cases for Base"""
    def test_id(self):
        self.assertEqual(Base(42).id, 42)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base("fffff").id, "fffff")
        self.assertEqual(Base(None).id, 3)


if __name__ == "__main__":
    unittest.main()
