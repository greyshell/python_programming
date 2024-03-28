import unittest
from remove_all_adjacent_duplicates_in_string import (
    solution,
)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        test_params = [
            ("ay", {"s": "azxxzy"}),
            ("ca", {"s": "abbaca"}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, solution(**kwargs))

