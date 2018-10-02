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

# declare global variables
my_global_array = []


def generate_strings_of_n_bits(low, high):
    """
    generate all binary strings of n-bits through backtracking (exploring all possibilities)
    time complexity: O(2^n)
    space complexity: O(2^n) => max length of the list / array
    :param low: int
    :param high: int
    :return: None
    """
    # declare to use global variables
    global my_global_array

    if high <= 0:
        print "[error] bit can't be zero or negative !!"
        exit(0)

    # traverse the depth of the tree
    elif low == high:
        print my_global_array
    else:
        # set the (n-1)th bit
        my_global_array[low] = 0
        generate_strings_of_n_bits(low + 1, high)  # this recursion leads to 0->0->0->.. n
        my_global_array[low] = 1
        generate_strings_of_n_bits(low + 1, high)


def main():
    # declare to use global variables
    global my_global_array

    string_of_bits = 2  # user input

    # use list comprehensions to generate a list based on the number of bits and fill with 0
    my_global_array = [0 for _ in range(0, string_of_bits)]
    generate_strings_of_n_bits(0, string_of_bits)


if __name__ == '__main__':
    main()
