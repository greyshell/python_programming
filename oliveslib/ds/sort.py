#!/usr/bin/python
# author: greyshell

"""
custom lib for sorting

"""


class CustomSort:
    def __init__(self):
        pass

    @staticmethod
    def selection_sort(my_list):
        """
        selection sort -> as it repeatedly selects the smallest element

        time complexity:
        worst case: O(n*n(n-2)/2) ~ O(n^2) -> when the list is sorted in reverse order
        average case: O(n^2)
        best case: O(n^2) -> when the list is sorted


        space complexity:
        worst case: O(1) -> in-place sort, no extra space is required

        features:
        1) in every iteration, it finds the smallest element from the list and place that in
        it's actual position.
        so, if we want to find the 5th smallest element then we can run the loop 5 times and returns
        my_list[0] -> 1st smallest element
        my_list[4] -> 5th smallest element

        after the kth iteration, the first k elements in the array are always in sorted order.
        this feature is very similar to insertion sort.

        2) comparison with insertion sort
        - Usually, insertion sort will perform less comparisons than selection sort, depending on the degree of
         sorted-ness of the array.  this is more often an advantage for insertion sort in that it runs much more
         efficiently if the array is already sorted or close to sorted.

        - One advantage of selection sort over insertion sort, is that the number of writes (swaps) is in O(n),
        while in insertion sort it is in O(n^2). This may be important if you are sorting on Flash memory,
        for example, because writes reduce the lifespan of Flash memory.

        - consider the cost of swaps against inserts: selection sort is the better alternative when using an array,
        while an insertion sort might perform better when using a linked list.

        3) A bidirectional variant of selection sort, called cocktail sort, is an algorithm which finds both the
        minimum and maximum values in the list in every pass. This reduces the number of scans of the list by a
        factor of 2, eliminating some loop overhead but not actually decreasing the number of comparisons or swaps.
        Note, however, that cocktail sort more often refers to a bidirectional variant of bubble sort. Sometimes this
        is double selection sort.

        4) selection sort is efficient on small list / array


        :param my_list[int]
        :return: my_list[int]
        """
        for i in range(0, len(my_list)):
            # consider current position has the minimum value
            index_of_smallest_element = i

            # find the index of the actual smallest element in the rest of the list
            for j in range(i + 1, len(my_list)):
                if my_list[j] < my_list[index_of_smallest_element]:
                    index_of_smallest_element = j

            if index_of_smallest_element != i:  # check to avoid unnecessary swap when the list is sorted
                # swap elements so that current position has the minimum value
                temp = my_list[index_of_smallest_element]
                my_list[index_of_smallest_element] = my_list[i]
                my_list[i] = temp

        return my_list

    @staticmethod
    def bubble_sort(my_list):
        """
        bubble sort (optimised) ->
        1. compare the adjacent elements and swap if left element is greater
        2. after first pass / iteration the max element has been bubbled up and placed into the last position
        3. after every pass, the array will be divided in to two part
            - sorted
            - unsorted -> iterate only this part

        time complexity:
        worst case: O((n-1)*(n-2)/2) ~ O(n^2) -> when the list is sorted in reverse order
        average case: O(n^2)
        best case: O(n-1) ~ O(n) -> when the list is already sorted,
        here we have used the swapped (bool) variable to skip the remaining passes.


        space complexity:
        worst case: O(1) -> in-place sort, no extra space is required

        features:
        1) good algorithm for sorted / partially sorted list as O(k*n). where k = 1, 2 ..
        as long as k as not big as n.


        :param my_list: int
        :return: my_list[int]
        """
        swapped = True
        i = len(my_list) - 1
        while i >= 0 and swapped is True:
            swapped = False
            j = 0
            while j <= (i - 1):  # avoid unnecessary iteration on sorted half
                if my_list[j] > my_list[j + 1]:
                    # swap the element
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                    swapped = True
                j += 1
            i -= 1
        return my_list


def main():
    """
    driver code to test the functionality
    :return:
    """
    a = CustomSort()
    print a.selection_sort([2, 1, 5, 3, 6, 12, 10, 14, 100])
    print a.bubble_sort([2, 1, 5, 300, 600, 12, 10, 14, 100])


if __name__ == '__main__':
    main()
