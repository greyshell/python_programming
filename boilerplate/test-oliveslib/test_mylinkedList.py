#!/usr/bin/env python
# author: greyshell

import unittest

from my_linkedList import SinglyLinkedList


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        optional:
        - run one time before staring the test
        - can be used to populate a database to set up testing
        :return:
        """
        pass

    def setUp(self):
        """
        optional:
        - run this before every single test function
        - can be used to add files to a directory / set variables
        :return:
        """
        self.s = SinglyLinkedList()
        pass

    def test_append(self):
        """
        verify the correctness of the solution
        :return:
        """
        s = SinglyLinkedList()
        s.append(3)
        s.append(4)

        self.assertEqual(str(s), "[3, 4]")

    def test_prepend(self):
        """
        verify the correctness of the solution
        :return:
        """
        s = SinglyLinkedList()
        s.append(2)
        s.prepend(1)
        self.assertEqual(str(s), "[1, 2]")

    def test_reverse_n(self):
        """
        verify the correctness of the solution
        :return:
        """
        self.s.append(2)
        self.s.append(3)
        self.s.append(4)
        self.s.append(5)
        self.s.reverse_n()

        self.assertEqual(str(self.s), "[5, 4, 3, 2]")

    def tearDown(self):
        """
        optional
        - it runs automatically after every single test function is executed
        - can be used to delete files from directory those created during testing / unset variables
        """
        self.s.cleanup()

    @classmethod
    def tearDownClass(cls):
        """
        optional ->
        can be used to clean up the database to start other testing from clean state
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
