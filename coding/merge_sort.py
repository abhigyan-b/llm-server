# filename: merge_sort.py
def merge_sort(arr):
    """Merge Sort: O(nlogn)

    :param arr: Input array to be sorted.
    :type arr: list
    :return: Sorted array.
    :rtype: list
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted arrays into one sorted array.

    :param left: Left sorted array.
    :type left: list
    :param right: Right sorted array.
    :type right: list
    :return: Merged sorted array.
    :rtype: list
    """

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    arr = [4, 1, 3, 2]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)