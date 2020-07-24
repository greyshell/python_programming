#!/usr/bin/env python3

# author: greyshell
# description: how to use stack ADT

from collections import deque as stack


def main():
    s = stack()
    # push: stack grows from right
    s.append(9)
    s.append(5)
    s.append(3)
    s.append(1)

    # display the stack elements
    print(f"display the stack elements: {list(s)}")

    # pop: stack shrinks from right
    data = s.pop()
    print(f"popped: {data}")

    print(f"display the stack elements: {list(s)}")

    # peek
    print(f"peek the stack top: {s[-1]}")


if __name__ == '__main__':
    main()
