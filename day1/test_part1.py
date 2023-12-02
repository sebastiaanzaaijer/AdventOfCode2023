import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
        self.assertEqual(solve_puzzle(example_input),142)
