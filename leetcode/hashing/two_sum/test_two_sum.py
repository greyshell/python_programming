#!/usr/bin/env python
# author: greyshell

import unittest
from .two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        """
        verify the solution
        :return:
        """
        self.assertEqual(Solution.two_sum([12, 7, 11, 15, 35], 50), [3, 4])
        self.assertEqual(Solution.two_sum([12, 7, 11, 15, 35], 19), [0, 1])
        self.assertEqual(Solution.two_sum([12, 7, 11, 15, 35], 89), [None, None])
        self.assertEqual(Solution.two_sum([12, 7, 11, -15, 35], 20), [3, 4])


if __name__ == '__main__':
    unittest.main()
