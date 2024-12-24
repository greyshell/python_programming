import unittest
from k_largest_elements_array import (
    get_k_largest_elements_array
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_get_k_largest_elements_array(self):
        # expected, actual
        test_params = [
            ([17, 16, 15, 14], {"array": [7, 17, 16, 2, 3, 15, 14], "k": 4}),
            ([70, 80, 90], {"array": [10, 20, 30, 50, 90, 70, 80, 40], "k": 3}),
            ([80, 90], {"array": [10, 20, 30, 50, 90, 70, 80, 40], "k": 2}),

        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertCountEqual(expected, get_k_largest_elements_array(**kwargs))


if __name__ == '__main__':
    unittest.main()
