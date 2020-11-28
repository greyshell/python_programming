#!/usr/bin/env python3
# author: greyshell
# how to run: python -m unittest test_blance_bracket.TestSolution

import unittest
from blance_bracket import solution


class TestSolution(unittest.TestCase):

    def test_solution_case_1(self):
        self.assertEqual(solution(['(', '(']), False)

    def test_solution_case_2(self):
        self.assertEqual(solution(['(', ')']), True)

    def test_solution_case_3(self):
        self.assertEqual(solution([')', '(']), False)

    def test_solution_case_4(self):
        self.assertEqual(solution(['(', '(', ')', ')']), True)

    def test_solution_case_5(self):
        self.assertEqual(solution([')', ')']), False)

    def test_solution_case_6(self):
        self.assertEqual(solution(['(', '(', ')', '(', ')']), False)

    def test_solution_case_7(self):
        self.assertEqual(solution(['(', ')', '(']), False)

    def test_solution_case_8(self):
        self.assertEqual(solution(['(', ')', ')']), False)

    def test_solution_case_9(self):
        self.assertEqual(solution(['(', '(', ')', '(', ')', ')']), True)


if __name__ == '__main__':
    unittest.main()
