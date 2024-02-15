#!/usr/bin/python3
"""Test Base model"""
import unittest
from models.base import Base


class testBase(unittest.TestCase):
    """test cases for Base"""
    def test_id_plus(self):
        self.assertEqual(Base(42).id, 42)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_id_minus(self):
        self.assertEqual(Base(-40).id, -40)
        self.assertEqual(Base(-9).id, -9)


if __name__ == "__main__":
    unittest.main()
