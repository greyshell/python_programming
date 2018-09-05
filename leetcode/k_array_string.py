#!/usr/bin/python

# author: greyshell
"""
[+] problem description
=======================
generate all the string of n bits

[+] reference
=============
Data Structures and Algorithm Made Easy by Narasimha, page 40

"""


def k_array_string(n, my_array):
    """
    generate all binary strings
    time complexity: O(2^n)
    :param n:
    :param my_array: list
    :return: list
    """
    if n < 0:  # base case 1
        print "[+] can't be negative"
        exit(0)
    elif n < 1:  # base case 2
        print "%s" % my_array
    else:
        # set (n - 1)th bit
        my_array[len(my_array) - 1] = 0
        k_array_string(n - 1, my_array)

        # unset (n - 1)th bit
        my_array[len(my_array) - 1] = 1
        k_array_string(n - 1, my_array)


def main():
    string_of_bits = 8  # user input
    # use list comprehensions to generate a list based on the number of bits
    my_array = [0 for _ in range(0, string_of_bits)]
    k_array_string(string_of_bits, my_array)


if __name__ == '__main__':
    main()
