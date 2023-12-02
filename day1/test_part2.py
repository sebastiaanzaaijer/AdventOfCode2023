import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        example_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
        self.assertEqual(solve_puzzle(example_input),281)

