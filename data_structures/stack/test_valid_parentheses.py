import unittest
from valid_parentheses import (
    solution,
)


class Test(unittest.TestCase):

    def test_solution(self):
        test_params = [
            (True, {"s": "()"}),
            (True, {"s": "(())"}),
            (True, {"s": "(()())"}),
            (False, {"s": "))"}),
            (False, {"s": ")("}),
            (False, {"s": "(("}),
            (False, {"s": "(()()"}),
            (False, {"s": "()("}),
            (False, {"s": "{[(])}"}),
            (True, {"s": "{{[[(())]]}}"}),
        ]

        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                self.assertEqual(expected, solution(**kwargs))
