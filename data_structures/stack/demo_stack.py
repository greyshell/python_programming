# !/usr/bin/env python3

# author: greyshell


def demo_stack():
    """
    - python list is backed by dynamic list, so occasionally it needs to be resized when item
    is added / removed
    - it does not guarantee the stable O(1) push and pop
    - however, it provides the amortize time complexity is O(1) when the item is added / remove at
    the end of list
    - adding / removing from front / middle is much slower and it takes O(n) time as shifting of
    existing elements
    are required
    - no parallel processing support / it handles locking and unlocking
    """
    stack = list()
    if len(stack) == 0:
        print('empty stack')

    # push: O(1), stack grows from left to right
    stack.append(9)
    stack.append(5)
    stack.append(3)
    stack.append(2)

    if len(stack):
        print('non empty stack')

    # display the stack elements
    print(f"display the stack elements: {stack}")

    # peek, O(1)
    data = stack[-1]  # peek the last element
    print(f"peek the stack top: {data}")

    # pop: O(1), stack shrinks from right to left
    # raise IndexError => pop from an empty list
    try:
        data = stack.pop()
        print(f"popped: {data}")
    except IndexError as e:
        print(f"{e}")

    print(f"display the stack elements: {list(stack)}")


def demo_stack_alt():
    from collections import deque
    """
    - deque is backed by doubly linked list
    - it that guarantees the stable O(1) push and pop
    - no parallel processing support / it handles locking and unlocking
    :return:
    """
    stack = deque()

    if len(stack) == 0:
        print('stack is empty')

    # push: O(1), stack grows from left to right
    stack.append(9)
    stack.append(5)
    stack.append(3)
    stack.append(1)

    if len(stack):
        print('non empty stack')

    # display the stack elements: convert the deque into list
    print(f"display the stack elements: {list(stack)}")

    # peek, O(1)
    data = stack[-1]
    print(f"peek the stack top: {data}")

    # pop: O(1), stack shrinks from right to left
    # raise IndexError => pop from an empty list
    try:
        data = stack.pop()
        print(f"popped: {data}")
    except IndexError as e:
        print(f"{e}")

    print(f"display the stack elements: {list(stack)}")


def demo_stack_alt2():
    from queue import LifoQueue
    """
    - used for parallel computing / multi producer and consumer scenarios
    - locking and un-locking needs to be implemented manually
    :return:
    """
    stack = LifoQueue()
    # push: O(1)
    stack.put(9)
    stack.put(2)

    # check if the stack is empty
    print(f"{stack.empty()}")

    # not found any method for peek and display stack elements

    # pop: O(1)
    # data = s.get_nowait()
    # data = s.get_nowait()

    try:
        data = stack.get_nowait()  # not wait for producer to add the element if the stack is empty
        print(f"popped: {data}")
    except Exception as e:
        print(f"{e}")

    # exit(0)

    # data = s.get()  # popped out the last stack element
    data = stack.get()  # waits for ever as the stack is empty, producer needs to add an element
    print(f"popped: {data}")


if __name__ == '__main__':
    demo_stack()
    # demo_stack_alt()
    # demo_stack_alt2()
