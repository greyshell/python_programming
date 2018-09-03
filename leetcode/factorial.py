#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
find the factorial of a number
1) recursive solution
2) tail recursive solution


[+] reference
=============
TBD

"""


class Solution(object):
    def tail_recursion_driver(self, n):
        """
        tail recursive solution
        :param n: int
        :return: int
        """
        return self.factorial_tail_recursion(n, 1)

    def factorial_tail_recursion(self, n, a):
        """
        :param n: int
        :param a: int => it accumulates the result
        :return: int
        """
        if n == 1:
            return a  # it carries the final result
        else:
            return self.factorial_tail_recursion(n - 1, n * a)

    def factorial(self, n):
        """
        normal recursive solution
        :return: int
        """
        if n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


def main():
    print Solution().tail_recursion_driver(5)
    print Solution().factorial(5)


if __name__ == '__main__':
    main()
