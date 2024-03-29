# author: greyshell
import unittest
from sorted_squared_array import sorted_squared_array


class TestProgram(unittest.TestCase):
    def test_solution(self):
        # expected, actual
        test_params = [
            ([1, 4, 9, 25, 36, 64, 81], {"array": [1, 2, 3, 5, 6, 8, 9]}),
            ([1, 4], {"array": [-2, -1]}),
            ([1, 4, 9, 16, 25], {"array": [-5, -4, -3, -2, -1]}),
        ]

        for expected, kwargs in test_params:
            self.subTest(**kwargs)
            self.assertEqual(expected, sorted_squared_array(**kwargs))


if __name__ == '__main__':
    unittest.main()
