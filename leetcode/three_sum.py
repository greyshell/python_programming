#!/usr/bin/python

# author: greyshell

"""
[+] problem description
=======================
Given an array of integers, return indices of the three numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

[+] example
===========

Given nums = [2, 7, 11, 15], target = 0,

Because nums[0] + nums[1] + num[2] = 2 + 7 + 11 = 20,
return [0, 1, 2]

[+] reference
=============


"""


def solution(num, target_sum):
    """
    time complexity: O(n^2), space complexity: O(n)
    :param num: List[int]
    :param target_sum: int
    :return: List[int]
    """
    lookup = {}

    # logic  => a + b = (sum - c)
    # store combination of all sums of two numbers in a dictionary, key = sum , number = list => two indexes
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            index = []
            t = num[i] + num[j]
            index.append(i)
            index.append(j)
            lookup[t] = index

    count = 0
    for n in num:
        t = target_sum - n
        if t in lookup:
            a = lookup[t]
            if count in a:  # avoid to use same element twice
                continue
            a.append(count)
            a.sort()
            return a
        count += 1

    return


def main():

    a = solution([2, 7, 11, 15], 20)
    if a:
        print "[+] indices are :"
        print a
    else:
        print "[x] sum not found"


if __name__ == '__main__':
    main()
