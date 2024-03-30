# author: greyshell
import unittest
from sort_stack import sort_stack


class TestProgram(unittest.TestCase):

    def test_solution(self):
        # expected, actual
        test_params = [
            ([-5, -2, 1, 2, 3, 4], {"stack": [-5, 2, -2, 4, 3, 1]}),
            ([-1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5],
             {"stack": [3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3]}),
            ([-9, -2, 0, 1, 1, 2, 4, 6, 22, 23], {"stack": [2, 4, 22, 1, -9, 0, 6, 23, -2, 1]}),
        ]

        for expected, kwargs in test_params:
            self.subTest(**kwargs)
            self.assertEqual(expected, sort_stack(**kwargs))


if __name__ == '__main__':
    unittest.main()
