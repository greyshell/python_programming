#!/usr/bin/env python3
# author: greyshell
# command: python -m unittest test_bfs.TestSolution

import unittest

from dfs import dfs, dfs_recursive


class TestSolution(unittest.TestCase):

    def setUp(self):
        """
        optional ->
        run this before every single test function
        can be used to add files to a directory / set variables
        """
        # ref: Sedgewick Algorithms 4th edition, page 532
        self.undirected_graph = {
            0: [2, 1, 5],
            1: [0, 2],
            2: [0, 1, 3, 4],
            3: [5, 4, 2],
            4: [3, 2],
            5: [3, 0]
        }

    def test_dfs(self):
        # order: assert(expected, actual)
        # ref: Sedgewick Algorithms 4th edition, page 532
        test_params = [
            ([0, 5, 3, 2, 4, 1], {"undirected_graph": self.undirected_graph, "start_vertex": 0}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, dfs(**kwargs))

    def test_dfs_recursive(self):
        # order: assert(expected, actual)
        # ref: Sedgewick Algorithms 4th edition, page 532
        test_params = [
            ([0, 2, 1, 3, 5, 4], {"undirected_graph": self.undirected_graph, "start_vertex": 0, "visited": []}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, dfs_recursive(**kwargs))


if __name__ == '__main__':
    unittest.main()
