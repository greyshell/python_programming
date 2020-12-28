#!/usr/bin/env python3

# author: greyshell
# description: how to use heapq library

import heapq


class Node(object):
    def __init__(self, val, index, name):
        self.val = val
        self.index = index
        self.name = name

    def __lt__(self, other):
        # tweak the comparison logic, so that when heapq use this it builds the max heap
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(0, len(nums))]


def main():
    min_heap = [12, 7, 11, 15, 35, 17]

    print(f"before heap sort: {min_heap}")
    r = heap_sort(min_heap)
    print(f"after heap sort: {r}")

    # build a min heap
    heapq.heapify(min_heap)  # in-place, in linear time, O(n), Heap elements can be tuples.

    # push an item
    heapq.heappush(min_heap, 25)  # O(log(n))
    heapq.heappush(min_heap, 5)  # O(log(n))
    heapq.heappush(min_heap, 10)  # O(log(n))

    # peek the min item
    data = min_heap[0]  # O(1)

    # pop an item
    data = heapq.heappop(min_heap)  # O(log(n))
    print(f"popped item: {data}")
    print(f"current heap : {min_heap}")

    # when we need to make the heap size constant, we can use heappushpop() and heapreplace()
    # time complexity: O(log(n)), improving the performance
    dummy_nums = min_heap.copy()  # copy all elements to another list
    data = -1
    popped_value = heapq.heappushpop(min_heap, data)  # 1st push then pop
    print(f"popped value: {popped_value}")

    popped_value = heapq.heapreplace(dummy_nums, data)  # 1st pop from existing min then push
    print(f"popped value: {popped_value}")

    # k largest / smallest elements
    # best for smaller values of k
    min_heap.append(100)
    min_heap.append(200)
    min_heap.append(50)
    print(f"nums = {min_heap}")

    large = heapq.nlargest(3, min_heap)
    small = heapq.nsmallest(3, min_heap)
    print(f"largest values: {large}, smallest values: {small}")
    # when k==1, it is more efficient to use the built-in min() and max() functions.

    # for larger k values it is more efficient to use the sorted() function.

    # kth largest element
    k = 4
    kth_large = heapq.nlargest(k, min_heap)
    print(f"{k}th largest value: {kth_large[k - 1]}")

    # create a max heap that stores an object (val, index, name) and the key is val
    max_heap = []

    heapq.heappush(max_heap, Node(17, 0, 'alice'))
    heapq.heappush(max_heap, Node(10, 0, 'bob'))
    heapq.heappush(max_heap, Node(25, 0, 'tom'))
    heapq.heappush(max_heap, Node(5, 0, 'rob'))

    print(f"max value {max_heap[0]}")
    node = heapq.heappop(max_heap)
    print(f"popped item: {node.val}")
    print(f"max value {max_heap[0]}")


if __name__ == '__main__':
    main()
