import unittest

from quxes_transformation import solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        test_params = [
            (['R'], {"arrangement": ['R', 'G', 'B', 'G', 'B']}),
            (['R', 'R', 'R'], {"arrangement": ['R', 'R', 'R']}),
        ]

        for expected, kwargs in test_params:
            self.subTest(**kwargs)
            self.assertEqual(expected, solution(**kwargs))
