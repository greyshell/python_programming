def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)


def k_smallest(arr, low, high, k):
    if low <= high:
        n = high - low + 1
        pi = partition(arr, low, high)
        elem_l = pi - low
        if k == elem_l + 1:
            return arr[pi]
        elif k < elem_l + 1:
            return k_smallest(arr, low, pi - 1, k)
        else:
            return k_smallest(arr, pi + 1, high, k - elem_l - 1)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
for i in range(n):
    print(k_smallest(arr, 0, n - 1, i+1))