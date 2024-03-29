def add_binary(num1: str, num2: str) -> str:
    """
    reference: https://leetcode.com/problems/add-binary/
    time: O(N + M), where N, M are the length of the input strings
    space: O(N + M)
    """
    n = max(len(num1), len(num2))
    # standardize the length
    num1 = num1.zfill(n)
    num2 = num2.zfill(n)

    carry = 0
    answer = []
    # iterate the loop from n-1 to 0
    for i in range(n - 1, -1, -1):
        if num1[i] == '1':
            carry += 1
        if num2[i] == '1':
            carry += 1

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        # carry = carry // 2 #  floor down
        carry //= 2

    if carry == 1:
        answer.append('1')

    answer.reverse()  # assuming O(1) -> inline reverse using two pointer

    return ''.join(answer)
