import unittest
from laptop_rentals import (
    laptop_rentals
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_laptop_rentals(self):
        # expected, actual
        test_params = [
            (3, {"times": [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]}),
            (1, {"times": [[5, 6], [4, 5], [3, 4], [2, 3], [1, 2]]}),

        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # ensures that both lists have the same elements, including duplicates, irrespective of their order.
                self.assertEqual(expected, laptop_rentals(**kwargs))


if __name__ == '__main__':
    unittest.main()
