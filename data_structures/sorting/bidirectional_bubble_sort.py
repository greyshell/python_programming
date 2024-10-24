
def bubble_sort(arr):
    """
    - compare adjacent elements and place the small element at the left.
     - after 1st pass of the outer loop, the smallest element bubbles up at the 0th index.
     - every pass of outer loop, builds up a small sorted array of small elements from left to right.
     - at any point of time if the program crashes then also we can get a sorted sub-array
        where all elements are placed in their actual positions.
     - in order to find kth small-est element, we need kth pass of the outer loop -> O(k*n)
     - effective on array data_arr structure not linked list
     - used for internal sorting: uses the main memory exclusively
     - stable: preserves the relative order of the duplicate items / keys,
        - interchange only occurs when the right_element < left_element
        - due to that, for duplicate keys, interchange does not happen
     - where cost (in terms of time complexity) of moving data_arr / swaps dominates the cost of making comparisons
        there bubble sort is not a good choice.
     - cocktail sort is a variation of bubble sort. minor performance improvement through bi-directional sort,
     - means bubbling up the smallest and the largest element in single pass.
     - although the all-time complexities are same, but insertion sort takes less swaps
     - comparing to bubble sort.
     - bubble is not use anywhere in real life.

     time complexity:
     ================
     *  - worst case / tight upper bound: when the input array is reversely sorted -> o(n^2)
     *      - 1st pass -> n comparisons and at most n swaps
     *      - 2nd pass -> n - 1 comparisons and at most n - 1 swaps
     *      - total comparisons =  n + (n -1) + (n-2) + .. 1 -> n*(n-1)/2 -> n^2
     *      - total swaps = n^2
     *  - best case / tight lower bound: when the input array is already sorted -> Ω(n)
     *      - total comparisons = (n-1)
     *      - total swaps = 0
     *      - adaptive: algorithm takes the advantage of 'existing order of input' to
     *      reduce the running time.
     *  - average case: considering the random distribution of elements -> o(n^2)
     *      - total comparisons = n^2
     *      - total swaps = n^2
     *  - not an optimal algorithm as best and worst case time complexities are different
     *
     * space complexity:
     * =================
     *  - in-place / in-memory sorting: no auxiliary space is required
     *  - non-recursive: call stack max depth -> none
     *  - takes constant time -> Θ(1): best and worst case space complexities are same.

    """
    pass


def bidirectional_bubble_sort(arr):
    """
    - bidirectional bubble sort / cocktail shaker sort / shuttle sort
    - the algorithm extends the bubble sort by operating in two directions.
    - time and space complexity is same as bubble sort
    - it is just a minor performance improvement => cocktail sort < 2 * bubble sort
    """

    if len(arr) == 0:
        raise ValueError("no element in array")

    # set up two pointers to traverse the array
    left_idx = 0
    right_idx = len(arr) - 1

    while True:
        is_swapped = False
        # objective of the while loop: push smaller element to left side of the array
        i = right_idx
        # decremental while loop
        while i > left_idx:
            # if the left element is greater than right then swap
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                # enable the swap flag
                is_swapped = True
            i -= 1

        # improvement: if the array is already sorted then we don't need to perform another iteration
        if not is_swapped:
            return arr

        # reset the swap flag
        is_swapped = False
        # at this point, left index already has the minimum value so increment the pointer
        left_idx += 1
        # objective of the while loop: push greater element to right side of the array

        # incremental while loop
        i = left_idx
        while i < right_idx:
            # if the right element is smaller than left then swap
            if arr[i + 1] < arr[i]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                # enable the swap flag
                is_swapped = True
            i += 1

        if not is_swapped:
            return arr

        # at this point, right index already has the max value so decrement the pointer
        right_idx -= 1


