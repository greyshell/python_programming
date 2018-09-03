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


def tail_recursion_driver(n):
    """
    tail recursive solution
    :param n: int
    :return: int
    """
    return factorial_tail_recursion(n, 1)  # 1 is used to start the first accumulation


def factorial_tail_recursion(n, a):
    """
    better than normal recursion as it could be optimized by the compiler by not saving the current stack frame
    :param n: int
    :param a: int => it accumulates the result
    :return: int
    """
    if n == 1 or n == 0:
        return a  # it carries the final result
    else:
        return factorial_tail_recursion(n - 1, n * a)


def factorial(n):
    """
    normal recursive solution
    :return: int
    """
    if n == 1 or n == 0:  # base case for n = 0, 1
        return 1
    else:  # recursive case when n > 1
        return n * factorial(n - 1)


def main():
    print tail_recursion_driver(12)
    print factorial(0)


if __name__ == '__main__':
    main()
