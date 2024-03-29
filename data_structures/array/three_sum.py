def three_sum(nums: list) -> bool:
    """
    write a function that takes an array of integers and returns a boolean based on whether
    there are 3 elements in it that sum to be 0
    time: O(n^2)
    space: O(1)
    """
    nums.sort()
    for i, num in enumerate(nums):
        start = i + 1
        end = len(nums) - 1
        while start < end:
            total = num + nums[start] + nums[end]
            if total == 0:
                return True
            elif total > 0:
                end -= 1
            elif total < 0:
                start += 1
    return False


if __name__ == "__main__":
    inp = [-1, -2, -5, 9, 3, -4]
    print(inp)
    out = three_sum(inp)
    print(out)
