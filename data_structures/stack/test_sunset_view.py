import unittest
from sunset_views import sunset_views


class TestProgram(unittest.TestCase):
    def test_solution(self):
        test_params = [
            ([1, 3, 6, 7], {"buildings": [3, 5, 4, 4, 3, 1, 3, 2], "direction": "EAST"}),
            ([3, 4], {"buildings": [1, 2, 3, 4, 1], "direction": "EAST"}),
        ]

        for expected, kwargs in test_params:
            self.subTest(**kwargs)
            self.assertEqual(expected, sunset_views(**kwargs))


if __name__ == '__main__':
    unittest.main()
