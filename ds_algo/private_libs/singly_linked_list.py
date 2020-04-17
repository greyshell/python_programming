#!/usr/bin/env python3

# author: greyshell


class ListNode:
    """
    a node in a singly-linked list, basic building block
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        """
        due to this magic method ListNode() does not return any address. such as
        <__main__.ListNode instance at 0x7f6faf943710>
        :return:
        """
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):  # traversing the list
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'  # return type is string

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next_node=self.head)  # returns the data

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:  # means head points to NULL / None
            self.head = ListNode(data=data)
            return
        # situation where head does not point to NULL
        # need to find the node (i.e last node)  where head points to null
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found coz loop stops when curr is None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:  # not enter into loop for first node
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:  # condition to delete the first node
            self.head = curr.next
        elif curr:  # found the node and curr is not None
            # when the key is not found in while loop then curr -> None
            # so control will not reach here
            prev.next = curr.next
            curr.next = None

    def remove_all(self):
        """
        empty the list
        :return:
        """
        # just set the head to None
        self.head = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def recursive_reverse(self):
        """
        reverse the list in-place. Takes O(n) time.
        not swapping the element
        """

        def reverse(curr):
            """

            :return: node
            """
            if curr.next is None:  # until reach the last node
                return curr

            # swap the 2nd last node and last node
            first_n = curr
            last_n = reverse(curr.next)

            curr.next.next = first_n
            curr.next = None
            return last_n

        # set the head to the last node
        self.head = reverse(self.head)
