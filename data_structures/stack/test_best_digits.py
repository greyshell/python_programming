import unittest
from best_digits import best_digits


class TestProgram(unittest.TestCase):
    def test_solution(self):
        test_params = [
            ("6839", {"number": "462839", "num_digits": 2}),
            ("98763", {"number": "129847563", "num_digits": 4}),
            ("9", {"number": "19", "num_digits": 1}),
            ("2", {"number": "22", "num_digits": 1}),
            ("49", {"number": "249", "num_digits": 1}),
            ("94", {"number": "942", "num_digits": 1}),
        ]

        for expected, kwargs in test_params:
            self.subTest(**kwargs)
            self.assertEqual(expected, best_digits(**kwargs))


if __name__ == '__main__':
    unittest.main()
