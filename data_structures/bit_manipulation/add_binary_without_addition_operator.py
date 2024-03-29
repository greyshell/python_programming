def add_binary_without_addition_operator(num1: str, num2: str) -> str:
    """
    reference: https://leetcode.com/problems/add-binary/
            - https://www.youtube.com/watch?v=qq64FrA2UXQ&list=PLiQ766zSC5jN42O1DBalnkom5y2LXtnnK&index=2
    Time: O(N + M), where N and M are lengths of the input strings a and b.
    Space: O(max(N,M)) to keep the answer.
    """
    #  convert both numbers in to integer of base 2 to apply bit operator
    x = int(num1, base=2)  # here we store the actual result
    y = int(num2, base=2)

    while y:
        # XOR operator simulates addition without carry
        answer_without_carry = x ^ y

        answer_without_carry_bin_format = bin(answer_without_carry)[2:]
        print(f"{answer_without_carry_bin_format}")
        """
        # 1 + 3 
        num1: 0001
        num2: 0011
        XOR -> exclusive OR -> like OR: T if either is T, 
                               unlike OR: when both are T it is F
        -----------
              0010
        """
        # AND operator discovers where carries are generated / where we need carries
        """
        # 1 + 3
        num1: 0001
        num2: 0011
        AND
        -----------
              0001 -> carry was generated at the 0th position
        """
        carry_generated = x & y
        carry_generated_bin_format = bin(carry_generated)[2:]

        print(f"{carry_generated_bin_format}")

        # left shift operator gives where we need to apply carry
        carry = carry_generated << 1

        carry_bin_format = bin(carry)[2:]
        print(f"{carry_bin_format}")

        y = carry
        x = answer_without_carry

        x_value_bin_format = bin(x)[2:]
        y_value_bin_format = bin(y)[2:]
        print(f"{x_value_bin_format}, {y_value_bin_format}")
        print()

    return bin(x)[2:]  # convert the number into binary after removing "0b" -> first two char


if __name__ == "__main__":
    n1 = '01'  # 1
    n2 = '11'  # 3
    out = add_binary_without_addition_operator(n1, n2)
    print(f"{out}")  # 1 + 3 = 4 -> 100
