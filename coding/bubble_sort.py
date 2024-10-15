# filename: bubble_sort.py
def bubble_sort(nums):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.

    Args:
        nums: A list of numbers to be sorted.

    Returns:
        The sorted list of numbers.
    """
    length = len(nums)

    for i in range(length):
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums