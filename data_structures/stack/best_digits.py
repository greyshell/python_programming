def best_digits(number, num_digits):
    stack = []

    for digit in number:

        while (num_digits > 0 and
               len(stack) > 0 and
               digit > stack[-1]):
            stack.pop()
            num_digits -= 1

        stack.append(digit)

    # cover ascending condition
    while num_digits > 0:
        stack.pop()
        num_digits -= 1

    return "".join(stack)