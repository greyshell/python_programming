# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

# import program
import unittest

from min_max_stack import MinMaxStack


class TestProgram(unittest.TestCase):

    def _test_min_max_peek(self, min, max, peek, stack):
        self.assertEqual(stack.get_min(), min)
        self.assertEqual(stack.get_max(), max)
        self.assertEqual(stack.peek(), peek)

    def test_operations(self):
        stack = MinMaxStack()
        stack.push(5)
        self._test_min_max_peek(5, 5, 5, stack)
        stack.push(7)
        self._test_min_max_peek(5, 7, 7, stack)
        stack.push(2)
        self._test_min_max_peek(2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        self._test_min_max_peek(5, 5, 5, stack)


if __name__ == '__main__':
    unittest.main()
