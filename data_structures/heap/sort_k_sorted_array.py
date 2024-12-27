#!/usr/bin/env python3

from libozone import Heap, HeapType


def sort_k_sorted_array(arr, k):
    """
    time: O(n*log(k))
    space: O(1)
    """
    min_array = arr[:min(k + 1, len(arr))]
    min_heap = Heap(min_array)

    next_index_to_insert_elm = 0
    for i in range(k + 1, len(arr)):
        min_elm = min_heap.remove()
        # update the arr -> in place
        arr[next_index_to_insert_elm] = min_elm
        next_index_to_insert_elm += 1

        current_elm = arr[i]
        min_heap.insert(current_elm)

    while min_heap:
        min_elm = min_heap.remove()
        arr[next_index_to_insert_elm] = min_elm
        next_index_to_insert_elm += 1

    return arr


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4, 7, 6, 5]
    k = 3
    out = sort_k_sorted_array(arr, k=3)
    print(out)
