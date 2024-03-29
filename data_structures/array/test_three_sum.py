import unittest
from three_sum import (
    three_sum
)


class Test(unittest.TestCase):
    """
    how to run: python -m unittest test_<file_name>.py
    """
    def test_three_sum(self):
        # expected, actual
        test_params = [
            (False, {"nums": [-4, -1, 2]}),
            (True, {"nums": [-1, 3, -2]}),
            (True, {"nums": [-1, -2, 3, 4, 5]}),
            (False, {"nums": [1, 2, 3, 4, 5]}),
            (False, {"nums": [-1, 2, 5]}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                self.assertEqual(expected, three_sum(**kwargs))


if __name__ == '__main__':
    unittest.main()