#!/usr/bin/env python3
# author: greyshell
# command: python -m unittest test_bfs.TestSolution

import unittest

from dfs import dfs


# noinspection PyGlobalUndefined
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        optional ->
        run one time before staring the test
        can be used to populate a database to set up testing
        """
        print("[+] Running setUpClass method")
        # ref: Sedgewick Algorithms 4th edition, page 532
        global undirected_graph
        undirected_graph = {
            0: [1, 2, 5],
            1: [0, 2],
            2: [0, 1, 4],
            3: [2, 4, 5],
            4: [2, 3],
            5: [0, 3]
        }

    def setUp(self):
        """
        optional ->
        run this before every single test function
        can be used to add files to a directory / set variables
        """
        print("[+] Running setUp method method")

    def test_dfs(self):
        # order: assert(expected, actual)
        # ref: Sedgewick Algorithms 4th edition, page 532
        test_params = [
            ([0, 5, 3, 4, 2, 1], {"undirected_graph": undirected_graph, "start_vertex": 0}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, dfs(**kwargs))

    def tearDown(self):
        """
        optional ->
        run this after every single test
        can be used to delete files from directory those created during testing / unset variables
        """
        print("[+] Running tearDown method")

    @classmethod
    def tearDownClass(cls):
        """
        optional ->
        can be used to clean up the database to start other testing from clean state
        """
        print("[+] Running tearDownClass method")


if __name__ == '__main__':
    unittest.main()
