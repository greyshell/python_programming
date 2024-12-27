import unittest
from sort_k_sorted_array import (
    sort_k_sorted_array
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_get_k_largest_elements_array(self):
        # expected, actual
        test_params = [
            ([1, 2, 3, 4, 5, 5, 6, 7], {"arr": [3, 2, 1, 5, 4, 7, 6, 5], "k": 3}),

        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertEqual(expected, sort_k_sorted_array(**kwargs))


if __name__ == '__main__':
    unittest.main()
