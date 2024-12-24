#!/usr/bin/env python3

# author: greyshell
import unittest
from continuous_median import MedianFinder


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_heap_operations_01(self):
        heap = MedianFinder()
        heap.add_num(1)
        self.assertEqual(1, heap.get_median())

        heap.add_num(2)
        self.assertEqual(1.5, heap.get_median())

        heap.add_num(3)
        self.assertEqual(2, heap.get_median())


if __name__ == '__main__':
    unittest.main()
