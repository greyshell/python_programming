#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

[+] example
===========

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

[+] reference
=============
- leetcode-001: https://leetcode.com/problems/two-sum/

"""


class Solution(object):

    def two_sum(self, nums, target):
        """
        description: time complexity: O(n), space complexity: O(n)
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        # create an empty dictionary
        hash_map = {}

        for index, n in enumerate(nums):
            complement = target - n
            # if the complement is not present in hash_map then insert the number as key, index as value
            if complement not in hash_map:
                hash_map[n] = index

            else:  # if found the complement in the hash_map then pick up the previous index
                prev_index = hash_map[complement]
                return [prev_index, index]

        # condition where target not found
        return [None, None]


def main():
    s = Solution()
    print s.two_sum([12, 7, 11, 15], 18)
    print s.two_sum([], 9)


if __name__ == '__main__':
    main()
