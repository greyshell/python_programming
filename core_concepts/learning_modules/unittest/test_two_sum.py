#!/usr/bin/env python3
# author: greyshell
# command: python -m unittest test_two_sum.TestSolution

import unittest
from two_sum import two_sum


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        optional ->
        run one time before staring the test
        can be used to populate a database to set up testing
        :return:
        """
        print("running setUpClass method")

    def setUp(self):
        """
        optional ->
        run this before every single test function
        can be used to add files to a directory / set variables
        :return:
        """
        print("running setUp method method")

    def test_case_1(self):
        """
        verify the correctness of the solution
        - actual -> means what we are providing into the assert statement
        - expected -> means what we are getting from the program
        :return:
        """
        self.assertEqual(two_sum([12, 7, 11, 15, 35], 50), [3, 4])

    def test_case_2(self):
        self.assertEqual(two_sum([12, 7, 11, 15, 35], 19), [0, 1])

    def tearDown(self):
        """
        optional ->
        run this after every single test
        can be used to delete files from directory those created during testing / unset variables
        :return:
        """
        print("running tearDown method")

    @classmethod
    def tearDownClass(cls):
        """
        optional ->
        can be used to clean up the database to start other testing from clean state
        :return:
        """
        print("running tearDownClass method")


if __name__ == '__main__':
    unittest.main()
