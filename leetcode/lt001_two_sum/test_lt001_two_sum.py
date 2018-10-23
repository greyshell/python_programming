import unittest
import lt001_two_sum as s


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        """
        verify the solution
        :return:
        """
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 50), [3, 4])
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 19), [0, 1])
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 89), None)
        self.assertEquals(s.two_sum([12, 7, 11, -15, 35], 20), [3, 4])

if __name__ == '__main__':
    unittest.main()
