#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
Given an array of integers, return indices of the three numbers such that they add up to a specific target.

You may assume that each input would have exactly one two_sum, and you may not use the same element twice.

[+] example
===========

Given nums = [2, 7, 11, 15], target = 0,

Because nums[0] + nums[1] + num[2] = 2 + 7 + 11 = 20,
return [0, 1, 2]

[+] reference
=============


"""


def three_sum(num, target_sum):
    """
    approach:
        - meat of the program -> (a + b) = (sum - c)
        - store the all possible sums of two elements in a hash table, key -> sum, value -> list[index of two numbers]
        - scan the list and find (the sum - k) in the hash table

    time complexity: O(n^2)
    space complexity: O(n) -> size of the hash table

    :param num: List[int]
    :param target_sum: int
    :return: List[int]
    """
    lookup = {}

    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            index = []
            t = num[i] + num[j]
            index.append(i)
            index.append(j)
            lookup[t] = index

    for i, n in enumerate(num):
        t = (target_sum - n)
        if t in lookup:
            indexes = lookup[t]
            print indexes
            # if i in indexes:  # avoid to use same element twice
            #     continue
            indexes.append(i)
            indexes.sort()
            return indexes

    # when target sum is not found, function implicit returns None
    return


def main():
    # program input
    input_list = [12, 7, 11, 15, 35]
    target_sum = 30

    print "[+] given list: ", input_list
    print "[+] given sum: ", target_sum

    out = three_sum(input_list, target_sum)

    # program output
    print "[+] output:", out


if __name__ == '__main__':
    main()
