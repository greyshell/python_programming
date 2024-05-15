#!/usr/bin/env python3
# author: greyshell
# description: demo Heap library

from snowowl import Heap, HeapType


if __name__ == '__main__':
    arr = [5, 9, 2]

    hmin = Heap(arr, HeapType.MIN)  # create a min heap
    print(f"peek={hmin.peek()}")  # peek the min item from the heap = 2
    hmin.insert(1)  # insert an item into the heap
    print(f"peek={hmin.peek()}")  # peek the min item from the heap = 1
    print(f"pop={hmin.remove()}")  # remove an item from the heap = 1
    hmin.insert(10)  # insert an item into the heap

    # how print works: does __getitems__() used
    print(hmin)  # print all items from the heap = [2, 9, 5, 10]
    print(f"length={len(hmin)}")  # print the length of the heap = 4
    print("")

    # what makes hmin iterable
    for i in hmin:
        print(i, end=" ")  # 2 9 5 10

    print("")

    hmax = Heap(arr, HeapType.MAX)  # create a max heap
    print(hmax.peek())  # peek the max item from the heap = 10
    hmax.insert(1)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap = 10
