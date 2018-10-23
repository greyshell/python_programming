import unittest
import lt001_two_sum as s


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        run one time before staring the test
        can be used to populate a database to set up testing
        :return:
        """
        pass

    def setUp(self):
        """
        run this before every single test function
        can be used to add files to a directory / set variables
        :return:
        """
        pass

    def test_two_sum(self):
        """
        verify the solution
        :return:
        """
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 50), [3, 4])
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 19), [0, 1])
        self.assertEquals(s.two_sum([12, 7, 11, 15, 35], 89), None)
        self.assertEquals(s.two_sum([12, 7, 11, -15, 35], 20), [3, 4])

    def tearDown(self):
        """
        run this after every single test
        can be used to delete files from directory those created during testing / unset variables
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        can be used to clean up the database to start other testing from clean state
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
