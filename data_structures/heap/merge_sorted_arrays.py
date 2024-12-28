#!/usr/bin/env python3

# author: greyshell

from libozone import Heap, HeapType


class Node:
    def __init__(self, array_index, element_index, num):
        self.array_index = array_index
        self.element_index = element_index
        self.key = num

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


def merge_sorted_arrays(arrays):
    """
    time: O(n*log(k) + log(k))
    space: O(n)
    """
    sorted_arrays = []
    smallest_items = []  # each item is Node obj

    for i in range(0, len(arrays)):
        node = Node(array_index=i, element_index=0, num=arrays[i][0])
        smallest_items.append(node)

    min_heap = Heap(smallest_items)  # O(k)

    while min_heap:  # O(n*log(k))
        smallest_item_node = min_heap.remove()
        # extract the property values
        array_index = smallest_item_node.array_index
        element_index = smallest_item_node.element_index
        num = smallest_item_node.key

        sorted_arrays.append(num)

        if element_index == (len(arrays[array_index]) - 1):
            continue
        else:
            element_index += 1
            # preparing the node
            node = Node(array_index, element_index, arrays[array_index][element_index])
            min_heap.insert(node)

    return sorted_arrays


if __name__ == '__main__':
    lists = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]
    out = merge_sorted_arrays(lists)
    print(out)
