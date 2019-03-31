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
        """
        pass

    def setUp(self):
        """
        optional:
        - run this before every single test function
        - can be used to add files to a directory / set variables
        """
        self.s_list = SinglyLinkedList()

    # ------------------- test methods --------------------- #

    def test_append(self):
        self.s_list.append(3)
        self.s_list.append(4)

        # assertEqual(expect, actual)
        self.assertEqual("[3, 4]", str(self.s_list))

    def test_prepend(self):
        self.s_list.prepend(2)
        self.s_list.prepend(1)
        self.s_list.prepend(0)

        # assertEqual(expect, actual)
        self.assertEqual("[0, 1, 2]", str(self.s_list))

    def test_reverse(self):
        self.s_list.append(2)
        self.s_list.append(3)
        self.s_list.append(4)
        self.s_list.append(5)

        self.s_list.reverse()

        # assertEqual(expect, actual)
        self.assertEqual("[5, 4, 3, 2]", str(self.s_list))

    def test_recursive_reverse(self):
        self.s_list.append(2)
        self.s_list.append(3)
        self.s_list.append(4)
        self.s_list.append(5)

        self.s_list.recursive_reverse()

        # assertEqual(expect, actual)
        self.assertEqual("[5, 4, 3, 2]", str(self.s_list))

    def test_find(self):
        self.s_list.append(3)
        self.s_list.append(4)

        # assertEqual(expect, actual)
        self.assertEqual("3", str(self.s_list.find(3)))

    def test_remove(self):
        self.s_list.append(3)
        self.s_list.append(4)
        self.s_list.append(5)
        self.s_list.append(3)

        self.s_list.remove(3)

        # assertEqual(expect, actual)
        self.assertEqual("[4, 5, 3]", str(self.s_list))  # remove the first element

    def test_remove_all(self):
        self.s_list.append(3)
        self.s_list.append(4)
        self.s_list.append(5)
        self.s_list.append(3)

        self.s_list.remove_all()
        self.assertEqual("[]", str(self.s_list))

    # ------------------- test methods --------------------- #

    def tearDown(self):
        """
        optional
        - it runs automatically after every single test function is executed
        - can be used to delete files from directory those created during testing / unset variables
        """
        self.s_list.remove_all()

    @classmethod
    def tearDownClass(cls):
        """
        optional ->
        can be used to clean up the database to start other testing from clean state
        """
        pass


if __name__ == '__main__':
    unittest.main()
