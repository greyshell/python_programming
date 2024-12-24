import unittest

from k_largest_elements_immutable_max_heap import (
    get_k_largest_elements_immutable_max_heap
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_get_k_largest_elements_immutable_max_heap(self):
        # expected, actual
        test_params = [
            ([17, 16, 15, 14], {"immutable_max_heap": [17, 7, 16, 2, 3, 15, 14], "k": 4}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertCountEqual(expected, get_k_largest_elements_immutable_max_heap(**kwargs))


if __name__ == '__main__':
    unittest.main()
