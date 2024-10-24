#!/usr/bin/env python3
# author: greyshell
# command: python -m unittest file_name.method_name

import unittest
from bidirectional_bubble_sort import bidirectional_bubble_sort


class TestProgram(unittest.TestCase):

    def test_bidirectional_bubble_sort(self):
        # order: assert(expected, actual)
        test_params = [
            ([7, 11, 12, 15, 35], {"arr": [12, 7, 11, 15, 35]}),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {"arr": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {"arr": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]}),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {"arr": [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]}),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], {"arr": [7, 3, 5, 1, 6, 2, 8, 0, 9, 4]}),
            ([0, 0, 1, 2, 2, 5, 7, 8, 9, 9], {"arr": [7, 0, 5, 1, 9, 2, 8, 0, 9, 2]}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, bidirectional_bubble_sort(**kwargs))


if __name__ == '__main__':
    unittest.main()
