from collections import deque

"""
ref: https://leetcode.com/problems/valid-parentheses/
"""


def valid_parentheses(string: str) -> bool:
    # The stack to keep track of opening brackets.
    stack = []
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    matching_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # For every bracket in the expression.
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # case 1
            if len(stack) == 0:
                return False
            # get the opening bracket corresponding to closing bracket and compare to stack top
            if matching_brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


if __name__ == "__main__":
    strings = ")()()"
    print(strings)
    print(f"{valid_parentheses(strings)}")
