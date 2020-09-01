# !/usr/bin/env python3

# author: greyshell

"""
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power
of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the
third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such
transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the
following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B']      | (R, G) -> B
['B', 'B', 'G', 'B']            | (B, G) -> R
['B', 'R', 'B']                  | (R, B) -> G
['B', 'G']                        | (B, G) -> R
['R']
"""

d = list()

count = 0


def transform(a, b):
    s = 82 + 71 + 66
    color = dict()
    color[82] = 'R'
    color[71] = 'G'
    color[66] = 'B'
    c = s - (ord(a) + ord(b))
    return color[c]


def backtrack(i, j):
    global count
    if len(d) == j:
        print(d)
        exit(0)
    elif d[i] != d[j]:
        a1 = d.pop(i)
        a2 = d.pop(i)
        c = transform(a1, a2)
        d.insert(i, c)
        count += 1
        return i
    elif d[i] == d[j]:
        k = backtrack(i + 1, j + 1)
        a1 = d.pop(k - 1)
        a2 = d.pop(k - 1)
        c = transform(a1, a2)
        d.insert(k - 1, c)
        count += 1
        return k - 1


def solution(quexes):
    """
    time complexity: O(n)
    space complexity: O(n) for the storing the
    :param quexes:
    :return:
    """
    global count
    for ch in quexes:
        d.append(ch)

    n = len(d)

    while count < n:
        if d[0] == d[1]:
            backtrack(0, 1)
        else:
            c = transform(d.pop(1), d.pop(0))
            d.insert(0, c)
        count += 1

    return d


def main():
    quxes = ['R', 'G', 'B', 'B', 'B', 'R']
    print(quxes)
    result = solution(quxes)
    print(f"{result}")


if __name__ == '__main__':
    main()
