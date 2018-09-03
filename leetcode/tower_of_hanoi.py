#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
tower of hanoi

[+] reference
=============
http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html

"""


class Solution(object):

    def toh(self, n, x, y, z):
        """
        time complexity: O(2^(n+1) -1 ) ~ O(2^n)
        space complexity: O(n-1)
        nos of recursive function invocation: 2^n - 1,  considering the base case => I(n) = 1 where n = 1
        nos of movement being done: 2^n -1, considering the base case => M(n) = 0 where n = 0

        :param n: int
        :param x: char
        :param y: char
        :param z: char
        :return: void / none
        """
        if n == 1:  # improve the nos of function invocation
            print "[+] move disk from %s to %s" % (x, y)
        elif n > 1:
            self.toh(n-1, x, z, y)
            print "[+] move disk from %s to %s" % (x, y)
            self.toh(n - 1, z, y, x)

        return


def main():
    s = Solution()
    s.toh(3, 'x', 'y', 'z')
    # s.toh(5, 'x', 'y', 'z')


if __name__ == '__main__':
    main()
