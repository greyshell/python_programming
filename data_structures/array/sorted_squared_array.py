# author: greyshell
def sorted_squared_array(array):
    sorted_squares = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    # fill the array in reverse order
    for i in range(len(array) - 1, -1, -1):
        # pick the small and large elements
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[i] = smaller_value * smaller_value
            smaller_value_idx += 1
        else:
            sorted_squares[i] = larger_value * larger_value
            larger_value_idx -= 1

    return sorted_squares
