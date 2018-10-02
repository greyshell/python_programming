#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[+] reference
=============
- leetcode-001: https://leetcode.com/problems/two-sum/

"""


def two_sum(nums, target):
    """
    approach:
        - scan the list and check the complement (sum - number) in a hash table
        - if not found then insert the entry(key -> number, value -> index) into the hash table
        - if found then prepare a list [current index, index of the complement]

    time complexity: O(n)
    space complexity: O(n) -> size of the hash table

    :param nums: List[int]
    :param target: int
    :return: List[int]
    """
    lookup = {}

    # use enumerate() to track the index
    for i, n in enumerate(nums):
        complement = target - n

        # if complement is not in dictionary then insert
        if complement not in lookup:
            lookup[n] = i

        # if found the complement then pick up index of that found complement
        else:
            index = lookup[complement]
            return [index, i]

    # when target sum is not found, function implicit returns None
    return


def main():
    # program input
    input_list = [12, 7, 11, 15, 35]
    target_sum = 50

    print "[+] given list: ", input_list
    print "[+] given sum: ", target_sum

    out = two_sum(input_list, target_sum)

    # program output
    print "[+] output:", out


if __name__ == '__main__':
    main()
