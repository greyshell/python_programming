#!/usr/bin/python

# author: greyshell
"""
[+] problem description
=======================
given an array, check whether the array is in sorted order

[+] reference
=============
Data Structures and Algorithm Made Easy by Narasimha, page 38

"""


def is_list_sorted_order(a):
    """
    :param a:
    :return: bool
    """
    l = len(a)
    if l == 1:  # base case
        return True

    if a[l - 1] < a[l - 2]:  # check the last and second most last element
        return False
    else:
        # send list to the recursive call by eliminating the last element
        return is_list_sorted_order(a[:-1])


def main():
    a = [1, 5, 3, 3, 5, 5]
    print is_list_sorted_order(a)


if __name__ == '__main__':
    main()
