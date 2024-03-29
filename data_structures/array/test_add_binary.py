import unittest
from add_binary import (
    add_binary,
)


class Test(unittest.TestCase):

    def test_add_binary(self):
        test_params = [
            ("100", {"num1": "001", "num2": "11"}),
            ("100", {"num1": "11", "num2": "1"}),
            ("10101", {"num1": "1010", "num2": "1011"}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, add_binary(**kwargs))


if __name__ == '__main__':
    unittest.main()