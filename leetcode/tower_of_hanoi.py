#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================


[+] reference
=============
http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html

"""


class Solution(object):

    def toh(self, n, x, y, z):
        """
        description: time complexity: O(2^n), space complexity:
        :param n:
        :param x:
        :param y:
        :param z:
        :return:
        """
        if n >= 1:
            self.toh(n-1, x, z, y)
            print "[+] move disk from %s to %s" % (x, y)
            self.toh(n - 1, z, y, x)

        return


def main():
    s = Solution()
    # s.toh(3, 'x', 'y', 'z')
    s.toh(5, 'x', 'y', 'z')


if __name__ == '__main__':
    main()
