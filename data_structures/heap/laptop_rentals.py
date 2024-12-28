#!/usr/bin/env python3

# author: greyshell

from libozone import Heap, HeapType


class Node:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.key = end_time

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


def laptop_rentals(times):
    """
    time: O(n*log(n))
    space: O(n)
    """
    if len(times) == 0:
        return 0

    # time: O(n * log(n))
    times.sort(key=lambda x: x[0])

    interval_array = list()
    # preparing nodes
    node = Node(start_time=times[0][0], end_time=times[0][1])
    interval_array.append(node)
    min_heap = Heap(interval_array)  # time: O(n)

    for index in range(1, len(times)):  # time: O(n*log(k)), k is the heap size
        current_interval = times[index]
        start_time = current_interval[0]
        end_time = current_interval[1]

        if min_heap.peek().key <= start_time:
            min_heap.remove()

        # preparing node
        current_interval_node = Node(start_time=start_time, end_time=end_time)
        min_heap.insert(current_interval_node)

    return len(min_heap)


if __name__ == '__main__':
    arrays = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
    out = laptop_rentals(arrays)
    print(out)
