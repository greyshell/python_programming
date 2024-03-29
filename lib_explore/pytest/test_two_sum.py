#!/usr/bin/env python3

# author: greyshell
# command: python -m pytest test_two_sum.py -v

import pytest
from two_sum import two_sum


def test_two_sum():
    # test case 1
    arr = [12, 7, 11, 15, 35]
    target = 50
    # order: assert expected, actual
    assert {3, 4} == set(two_sum(arr, target))

    # testcase 2
    arr = [12, 7, 11, 15, 35]
    target = 19
    assert {0, 1} == set(two_sum(arr, target))

    # testcase 3
    arr = [12, 7, 11, 15, 35]
    target = 190
    expected_index = [None, None]
    assert {None, None} == set(two_sum(arr, target))

# def test_case_1() -> None:
#     arr = [12, 7, 11, 15, 35]
#     target = 50
#     expected_index = [3, 4]
#     assert set(two_sum(arr, target)) == set(expected_index)
#
#
# def test_case_2() -> None:
#     arr = [12, 7, 11, 15, 35]
#     target = 19
#     expected_index = [0, 1]
#     assert set(two_sum(arr, target)) == set(expected_index)
#
#
# def test_case_3() -> None:
#     arr = [12, 7, 11, 15, 35]
#     target = 190
#     expected_index = [None, None]
#     assert set(two_sum(arr, target)) == set(expected_index)
