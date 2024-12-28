import unittest
from merge_sorted_arrays import (
    merge_sorted_arrays
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_merge_sorted_arrays(self):
        # expected, actual
        test_params = [
            ([-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150],
             {"arrays": [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]}),

        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertEqual(expected, merge_sorted_arrays(**kwargs))


if __name__ == '__main__':
    unittest.main()
