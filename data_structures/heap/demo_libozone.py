#!/usr/bin/env python3
# description: demo heap
# author: greyshell

from libozone import Heap, HeapType


class Student:
    """helper class"""
    def __init__(self, name, score):
        self.name = name
        self.key = score

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


if __name__ == '__main__':
    arr = [5, 9, 2]

    hmin = Heap(arr)  # create a min heap
    print(hmin.peek())  # peek the min item from the heap -> 2
    hmin.insert(1)  # insert an item into the heap
    print(hmin.remove())  # remove an item from the heap -> 1
    print(hmin)  # print all items from the heap -> [2, 9, 5]
    print(len(hmin))  # print the length of the heap -> 3

    hmax = Heap(arr, HeapType.MAX)  # create a max heap
    print(hmax.peek())  # peek the max item from the heap -> 9
    hmax.insert(10)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap -> 10

    alice = Student(name="alice", score=80)
    bob = Student("bob", 90)
    malory = Student("malory", 75)
    tom = Student("tom", 85)

    arr = [alice, bob, malory, tom]
    student_heap = Heap(arr, HeapType.MAX)

    print(student_heap.peek().key)  # peek the max item from the heap -> 90
    ram = Student("ram", 95)
    student_heap.insert(ram)  # insert an item into the heap
    print(student_heap.remove().key)  # remove an item from the heap -> 95
