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
        """
        print("running setUpClass method")

    def setUp(self):
        """
        optional ->
        run this before every single test function
        can be used to add files to a directory / set variables
        """
        print("running setUp method method")

    def test_two_sum(self):
        # order: assert(expected, actual)
        # testcase 1
        self.assertEqual([3, 4], two_sum([12, 7, 11, 15, 35], 50))

        # testcase 2
        self.assertEqual([0, 1], two_sum([12, 7, 11, 15, 35], 19))

    def tearDown(self):
        """
        optional ->
        run this after every single test
        can be used to delete files from directory those created during testing / unset variables
        """
        print("running tearDown method")

    @classmethod
    def tearDownClass(cls):
        """
        optional ->
        can be used to clean up the database to start other testing from clean state
        """
        print("running tearDownClass method")


if __name__ == '__main__':
    unittest.main()
