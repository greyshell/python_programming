#!/usr/bin/env python3
# author: greyshell
# description: demo Heap library

from snowowl import Heap, HeapType


if __name__ == '__main__':
    arr = [5, 9, 2]

    hmin = Heap(arr, HeapType.MIN)  # create a min heap
    print(hmin.peek())  # peek the min item from the heap
    hmin.insert(1)  # insert an item into the heap
    print(hmin.peek())  # peek the min item from the heap
    print(hmin.remove())  # remove an item from the heap
    print(hmin)  # print all items from the heap
    print(len(hmin))  # print the length of the heap

    hmax = Heap(arr, HeapType.MAX)  # create a max heap
    print(hmax.peek())  # peek the max item from the heap
    hmax.insert(1)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap

