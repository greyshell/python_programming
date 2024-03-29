import unittest
from remove_all_adjacent_duplicates import (
    remove_all_adjacent_duplicates,
)


class TestProgram(unittest.TestCase):
    def test_solution(self):
        test_params = [
            ("ay", {"s": "azxxzy"}),
            ("ca", {"s": "abbaca"}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, remove_all_adjacent_duplicates(**kwargs))


if __name__ == '__main__':
    unittest.main()