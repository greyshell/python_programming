#!/usr/bin/env python3

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


class Solution:
    @staticmethod
    def two_sum(nums: list, target: int) -> list:
        """
        approach:
        - during scanning the list and check the complement (sum - number) in a hash table
        - if not found then insert the entry(key -> number, value -> index) into the hash table
        - if found then prepare a list [current index, index of the complement] and return

        time complexity: O(n)
        space complexity: O(n) -> size of the hash table
        """
        # create a hash_map ~ dictionary
        hash_map = {}

        for index, n in enumerate(nums):
            complement = target - n
            # if the complement is not present in hash_map then insert the number as key, index as value
            if complement not in hash_map:
                hash_map[n] = index

            else:  # found the complement in the hash_map
                prev_index = hash_map[complement]
                return [prev_index, index]

        # default scenario where target is not found
        return [None, None]  # returns a list


def main():
    """
    test the solution
    :return:
    """
    input_list = [12, 7, 11, 15, 35]
    target_sum = 50
    result = Solution.two_sum(input_list, target_sum)

    print(f"{result}")  # result: [3, 4]


if __name__ == '__main__':
    main()
