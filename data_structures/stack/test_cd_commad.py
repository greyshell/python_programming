import unittest
from cd_command import (
    cd_command,
)


class Test(unittest.TestCase):

    def test_solution(self):
        test_params = [
            ("/foo", {"cwd": "/", "arg": "foo"}),
            ("/bar", {"cwd": "/baz", "arg": "/bar"}),
            ("/", {"cwd": "/foo/bar", "arg": "../../../../.."}),  # non-empty stack
            ("/x/q", {"cwd": "/x/y", "arg": "../p/../q"}),   # non-empty stack
            ("/p/q", {"cwd": "/x/y", "arg": "/p/./q"}),

            # extra test cases
            ("/a", {"cwd": "/", "arg": "a"}),
            ("/a", {"cwd": "/", "arg": "/a"}),
            ("/b", {"cwd": "/a", "arg": "/b"}),
            ("/", {"cwd": "/lol", "arg": "../../../.."}),
            ("/foo/baz/x", {"cwd": "/foo", "arg": "bar/../baz/./x"}),
            ("/q", {"cwd": "/x", "arg": "/p/../q"}),
            ("/etc", {"cwd": "/foo/bar", "arg": "../../../../../../../../../../../etc"}),
        ]
        for expected, kwargs in test_params:
            with self.subTest(**kwargs):
                # expected, actual
                self.assertEqual(expected, solution(**kwargs))
