#!/usr/bin/python
# author: greyshell

"""
[+] problem description
=======================
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one two_sum, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[+] reference
=============
- leetcode-001: https://leetcode.com/problems/two-sum/

"""


def two_sum(nums, target_sum):
    """
    approach:
        - scan the list and check the complement (sum - number) in a hash table
        - if not found then insert the entry(key -> number, value -> index) into the hash table
        - if found then prepare a list [current index, index of the complement] and return

    time complexity: O(n)
    space complexity: O(n) -> size of the hash table

    :param nums: List[int]
    :param target_sum: int
    :return: List[int] / None
    """
    lookup = {}

    # use enumerate() to track the index
    for i, n in enumerate(nums):
        complement = target_sum - n

        # if complement is not in dictionary then insert
        if complement not in lookup:
            lookup[n] = i

        # if found the complement then pick up index of that found complement
        else:
            index = lookup[complement]
            return [index, i]

    # when target_sum sum is not found, return None
    return


def main():
    input_list = [12, 7, 11, 15, 35]
    target_sum = 50
    print two_sum(input_list, target_sum)


if __name__ == '__main__':
    main()
