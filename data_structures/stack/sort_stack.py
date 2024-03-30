#!/usr/bin/env python3

# author: greyshell
def _insert_in_sorted_order(stack, value):
    if (len(stack) == 0 or
            stack[-1] <= value):
        stack.append(value)
        return
    top = stack.pop()
    _insert_in_sorted_order(stack, value)
    stack.append(top)


def sort_stack(stack):
    """
    O(n^2) time | O(n) space
    """
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sort_stack(stack)

    _insert_in_sorted_order(stack, top)

    return stack
