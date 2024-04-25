"""
Best Digits
Write a function that takes a positive integer represented as a string number and an integer
numDigits.
Remove numDigits from the string so that the number represented by the string is as large as possible
afterwards.
Note that the order of the remaining digits cannot be changed.
You can assume numDigits will always be less than the length of number and greater than or equal to 0.

Sample Input
number = "462839" numDigits = 2
Sample Output
"6839" // remove digits 4 and 2
"""


def best_digits(number, num_digits):
    stack = []

    for digit in number:

        while num_digits > 0 and len(stack) > 0 and digit > stack[-1]:
            stack.pop()
            num_digits -= 1

        stack.append(digit)

    # cover descending condition: 987-65, next digit is always smaller than the stack top
    while num_digits > 0:
        stack.pop()
        num_digits -= 1

    return "".join(stack)
