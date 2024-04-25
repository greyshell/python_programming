import unittest
from check_valid_parentheses import (
    valid_parentheses,
)


class TestProgram(unittest.TestCase):

    def test_solution(self):
        test_params = [
            (True, {"string": "()"}),
            (True, {"string": "(())"}),
            (True, {"string": "(()())"}),
            (False, {"string": "))"}),
            (False, {"string": ")("}),
            (False, {"string": "(("}),
            (False, {"string": "(()()"}),
            (False, {"string": "()("}),
            (False, {"string": "{[(])}"}),
            (True, {"string": "{{[[(())]]}}"}),
            (False, {"string": "(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}}))))))"})
        ]

        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                self.assertEqual(expected, valid_parentheses(**kwargs))


if __name__ == '__main__':
    unittest.main()