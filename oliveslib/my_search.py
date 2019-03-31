#!/usr/bin/env python


class BinarySearch:
    """
    implementation of binary search
    """

    @staticmethod
    def iterative_approach(mylist, item):
        # low and high keep track of which part of the mylist you'll search in.
        low = 0
        high = len(mylist) - 1

        # while you haven't narrowed it down to one element ...
        while low <= high:  # single element
            # check the middle element
            mid = (low + high) / 2  # round off value
            guess = mylist[mid]
            # found the item.
            if guess == item:
                return mid
            # the guess was too high.
            elif guess > item:
                high = mid - 1
            # the guess was too low.
            elif guess < item:
                low = mid + 1

        # item doesn't exist
        return None
