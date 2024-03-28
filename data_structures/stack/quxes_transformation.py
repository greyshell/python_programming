"""
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""


from collections import deque


QUXES = {"R", "G", "B"}


def _transform(qux1: str, qux2: str) -> str:
    if qux1 == qux2:
        raise ValueError("Cannot form new Qux")
    result = QUXES - {qux1, qux2}
    return result.pop()  # return the first element in the set


def solution(arrangement):
    stack = deque()
    for qux in arrangement:
        if (len(stack) == 0 or   # stack is empty
                stack[-1] == qux):  # stack peek
            stack.append(qux)
        else:
            qux_last = stack.pop()
            while True:
                # back_propagating in case the previous quxes needs to be updated
                qux = _transform(qux_last, qux)
                if (len(stack) == 0 or
                        stack[-1] == qux):
                    break
                qux_last = stack.pop()
            stack.append(qux)
    # convert the deque object to list
    out = list(stack)
    return out


