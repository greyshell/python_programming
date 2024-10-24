def partition(arr, left, right):
    pivot = arr[right]
    # i => keep track of the tail of the section where items are less than pivot
    i = left - 1

    # scan the arr from left to right
    j = left
    while j < right:
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1

    # after the loop, i points to the last swapped element that less that pivot
    # (i + 1) points the element greater than pivot
    # less than pivot | pivot | greater than pivot: therefore (i + 1) is pivot position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def recursive_engine(arr, left, right):
    if left < right:
        pivot_position = partition(arr, left, right)
        if pivot_position > 0:  # optimization
            recursive_engine(arr, left, pivot_position - 1)

        recursive_engine(arr, pivot_position + 1, right)


def quick_sort(arr):
    left = 0
    right = len(arr) - 1
    recursive_engine(arr, left, right)
    return arr


arr = [3, 2, 1, 5, 6, 7]
out = quick_sort(arr)
print(out)

